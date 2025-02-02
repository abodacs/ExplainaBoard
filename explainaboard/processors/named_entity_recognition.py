from typing import Iterable
from explainaboard import feature
from explainaboard.tasks import TaskType
from explainaboard.processors.processor import Processor
from explainaboard.processors.processor_registry import register_processor
from explainaboard.builders.named_entity_recognition import NERExplainaboardBuilder

@register_processor(TaskType.named_entity_recognition)

class NERProcessor(Processor):
    _task_type = TaskType.named_entity_recognition
    _features = feature.Features({
        "tokens": feature.Sequence(feature.Value("string")),
        "ner_true_tags":feature.Sequence(feature.ClassLabel(names=[
            "O",
            "B-PER",
            "I-PER",
            "B-ORG",
            "I-ORG",
            "B-LOC",
            "I-LOC",
            "B-MISC",
            "I-MISC",
        ])),
        "ner_pred_tags": feature.Sequence(feature.ClassLabel(names=[
            "O",
            "B-PER",
            "I-PER",
            "B-ORG",
            "I-ORG",
            "B-LOC",
            "I-LOC",
            "B-MISC",
            "I-MISC",
        ])),
        "sentence_length": feature.Value(dtype="float",
                                         description="sentence length",
                                         is_bucket=True,
                                         bucket_info=feature.BucketInfo(
                                             _method="bucket_attribute_specified_bucket_value",
                                             _number=4,
                                             _setting=())),
        "true_entity_info":feature.Sequence(feature.Set({
            "span_text":feature.Value("string"),
            "span_len":feature.Value(dtype="float",
                                     description="entity length",
                                         is_bucket=True,
                                         bucket_info=feature.BucketInfo(
                                             _method="bucket_attribute_specified_bucket_value",
                                             _number=4,
                                             _setting=())),
            "span_pos":feature.Position(positions=[0,0]),
            "span_tag":feature.Value("string"),
            "eCon":feature.Value(dtype="float",
                                 description="entity label consistency",
                                         is_bucket=True,
                                         is_pre_computed=True,
                                         bucket_info=feature.BucketInfo(
                                             _method="bucket_attribute_specified_bucket_value",
                                             _number=4,
                                             _setting=())),
            "eFre":feature.Value(dtype="float",
                                 description="entity frequency",
                                         is_bucket=True,
                                         is_pre_computed=True,
                                         bucket_info=feature.BucketInfo(
                                             _method="bucket_attribute_specified_bucket_value",
                                             _number=4,
                                             _setting=())),
        }))
    })

    def __init__(self, metadata: dict, system_output_data: Iterable[dict]) -> None:
        if metadata == None:
            metadata = {}
        if "task_name" not in metadata.keys():
            metadata["task_name"] = TaskType.named_entity_recognition.value
        if "metric_names" not in metadata.keys():
            metadata["metric_names"] = ["f1_score_seqeval"]
        super().__init__(metadata, system_output_data)
        self._builder = NERExplainaboardBuilder(self._system_output_info, system_output_data)