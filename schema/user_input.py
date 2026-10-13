from pydantic import BaseModel, Field, field_validator
from typing import Literal, Annotated, Optional

from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional


class CustomerData(BaseModel):

    gender: Literal["Male", "Female"]

    SeniorCitizen: Literal[0, 1]

    Partner: Literal["Yes", "No"]

    Dependents: Literal["Yes", "No"]

    PhoneService: Literal["Yes", "No"]

    MultipleLines: Literal[
        "Yes",
        "No",
        "No phone service"
    ]

    InternetService: Literal[
        "DSL",
        "Fiber optic",
        "No"
    ]

    OnlineSecurity: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    OnlineBackup: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    DeviceProtection: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    TechSupport: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    StreamingTV: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    StreamingMovies: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    Contract: Literal[
        "Month-to-month",
        "One year",
        "Two year"
    ]

    PaperlessBilling: Literal["Yes", "No"]

    PaymentMethod: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]

    tenure: int = Field(ge=0)

    MonthlyCharges: float = Field(ge=0)

    TotalCharges: float | None = Field(default=None, ge=0)

    # Handle cases where TotalCharges comes in as " "
    @field_validator("TotalCharges", mode="before")
    @classmethod
    def handle_missing_total_charges(cls, value):
        if value is None:
            return None

        if isinstance(value, str) and not value.strip():
            return None

        return value