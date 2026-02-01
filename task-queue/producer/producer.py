from distributed_task_queue.domain.task import TaskRecord
from distributed_task_queue.domain.enums import TaskStatus
from distributed_task_queue.storage.client import redis_client
import uuid
import json


class TaskProducer:

    def __init__(self):
        self.client = redis_client()
        self.stream_name = "stream:tasks"


    def submit_task(self, task_name: str, payload: dict, max_attempts =3 , timeout_s=300) -> str:
        
        task = TaskRecord.create_task(
            task_name=task_name,
            payload_json=json.dumps(payload),
            status=TaskStatus.PENDING,
            max_attempts=max_attempts,
            timeout_s=timeout_s,
        )

        task_key = f"task:{task.id}"
