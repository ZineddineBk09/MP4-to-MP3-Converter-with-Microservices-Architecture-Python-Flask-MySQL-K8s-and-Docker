import pika, json


def upload(file, file_system, queue_channel, access):
    # save file to mongo gridfs
    try:
        file_id = file_system.put(file)
    except Exception as e:
        return f"failed to save file to gridfs: {e}", 500

    # save file metadata to mongodb
    try:
        file_data = {
            "video_fid": file_id,
            "mp3_fid": None,
            "filename": file.filename,
            "user_id": access["username"],
        }

        # publish file metadata to storage queue
        file_data = json.dumps(file_data)
        queue_channel.basic_publish(
            exchange="",
            routing_key="video",
            body=file_data,
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as e:
        # remove file from gridfs if metadata fails to save
        file_system.delete(file_id)
        return f"failed to save file metadata to mongodb: {e}", 500

    return None
