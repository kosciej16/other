# from ruamel.yaml import YAML
import yaml

# from pydantic import create_model
from pydantic import create_model

from langchain_core.pydantic_v1 import BaseModel, ConfigDict, Field, create_model


# from pydantic import create_model
# from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Literal, List
# TODO: this class was extrated from master script and contains question definition
# Extraction was performed due to inability to build the class from yaml definition.
# The target approach is to include such a class in master script and build it dynamically


def create_question_analysis_class(questions_definition: dict):
    """
    Metaclass function to create a QuestionAnalysis class with custom field descriptions.

    :param questions_definition: A dictionary mapping field names to their descriptions.
    :return: A new QuestionAnalysis class with customized field descriptions.
    """

    fields = {
        "id": (str, Field(description="question_id")),
        "text_comprehension": (
            eval(questions_definition["text_comprehension"]["type"]),
            Field(description=questions_definition["text_comprehension"]["desc"]),
        ),
        "text_adequateness": (
            eval(questions_definition["text_adequateness"]["type"]),
            Field(description=questions_definition["text_adequateness"]["desc"]),
        ),
        "reasons_clearness": (
            eval(questions_definition["reasons_clearness"]["type"]),
            Field(description=questions_definition["reasons_clearness"]["desc"]),
        ),
        "reason_main_category": (
            eval(questions_definition["reason_main_category"]["type"]),
            Field(description=questions_definition["reason_main_category"]["desc"]),
        ),
        "reason_categories": (
            eval(questions_definition["reason_categories"]["type"]),
            Field(description=questions_definition["reason_categories"]["desc"]),
        ),
        # "id": (str, Field()),  # `...` indicates that this field is required
        # "name": (str, ...),  # `...` indicates that this field is required
    }

    QuestionAnalysis = create_model("QuestionAnalysis", **fields)

    # class QuestionAnalysis(BaseModel):
    #     id: str = Field(description="question_id")
    #
    #     text_comprehension: eval(questions_definition["text_comprehension"]["type"]) = Field(
    #         description=questions_definition["text_comprehension"]["desc"]
    #     )
    #     text_adequateness: eval(questions_definition["text_adequateness"]["type"]) = Field(
    #         description=questions_definition["text_adequateness"]["desc"]
    #     )
    #     reasons_clearness: eval(questions_definition["reasons_clearness"]["type"]) = Field(
    #         description=questions_definition["reasons_clearness"]["desc"]
    #     )
    #     reason_main_category: eval(questions_definition["reason_main_category"]["type"]) = Field(
    #         description=questions_definition["reason_main_category"]["desc"]
    #     )
    #     reason_categories: eval(questions_definition["reason_categories"]["type"]) = Field(
    #         description=questions_definition["reason_categories"]["desc"]
    #     )
    #
    # build list of analysers
    class QuestionsAnalysis(BaseModel):
        model_config = ConfigDict(arbitrary_types_allowed=True)
        results_of_question_analysis: list[QuestionAnalysis]

    return QuestionsAnalysis


with open("som.yaml") as f:
    d = yaml.safe_load(f)

# print(d)
res = create_question_analysis_class(d["questions"])
print(res)
