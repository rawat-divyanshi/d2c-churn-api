from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(
    title="D2C Churn Prediction API",
    description="Customer churn prediction service",
    version="1.0"
)

# Load model at startup
model = joblib.load("models/model.pkl")


class CustomerFeatures(BaseModel):
    recency_days: float
    frequency_180d: float
    monetary_180d: float
    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float
    category_diversity_180d: float
    ticket_count_90d: float
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float
    days_since_signup: float
    sessions_30d: float
    product_views_30d: float
    cart_adds_30d: float
    wishlist_adds_30d: float
    abandoned_carts_30d: float
    email_opens_30d: float
    campaign_clicks_30d: float
    last_visit_days_ago: float

    city_tier_Tier_2: int
    city_tier_Tier_3: int

    age_group_25_34: int
    age_group_35_44: int
    age_group_45_plus: int

    acquisition_channel_Influencer: int
    acquisition_channel_Instagram: int
    acquisition_channel_Marketplace: int
    acquisition_channel_Organic: int
    acquisition_channel_Referral: int

    loyalty_tier_Platinum: int
    loyalty_tier_Silver: int

    preferred_category_Fragrance: int
    preferred_category_Hair_Care: int
    preferred_category_Makeup: int
    preferred_category_Skin_Care: int
    preferred_category_Wellness: int

    marketing_consent_Yes: int


@app.get("/")
def home():
    return {"message": "D2C Churn Prediction API Running"}


@app.get("/health")
def health():
    return {"status": "ok"}
@app.post("/predict")
def predict(data: CustomerFeatures):

    features = [[
        data.recency_days,
        data.frequency_180d,
        data.monetary_180d,
        data.return_rate_180d,
        data.avg_discount_pct_180d,
        data.avg_rating_180d,
        data.category_diversity_180d,
        data.ticket_count_90d,
        data.negative_ticket_rate_90d,
        data.avg_resolution_hours_90d,
        data.days_since_signup,
        data.sessions_30d,
        data.product_views_30d,
        data.cart_adds_30d,
        data.wishlist_adds_30d,
        data.abandoned_carts_30d,
        data.email_opens_30d,
        data.campaign_clicks_30d,
        data.last_visit_days_ago,
        data.city_tier_Tier_2,
        data.city_tier_Tier_3,
        data.age_group_25_34,
        data.age_group_35_44,
        data.age_group_45_plus,
        data.acquisition_channel_Influencer,
        data.acquisition_channel_Instagram,
        data.acquisition_channel_Marketplace,
        data.acquisition_channel_Organic,
        data.acquisition_channel_Referral,
        data.loyalty_tier_Platinum,
        data.loyalty_tier_Silver,
        data.preferred_category_Fragrance,
        data.preferred_category_Hair_Care,
        data.preferred_category_Makeup,
        data.preferred_category_Skin_Care,
        data.preferred_category_Wellness,
        data.marketing_consent_Yes
    ]]

@app.post("/batch_predict")
def batch_predict(data_list: list[CustomerFeatures]):

    results = []

    for data in data_list:

        features = [[
            data.recency_days,
            data.frequency_180d,
            data.monetary_180d,
            data.return_rate_180d,
            data.avg_discount_pct_180d,
            data.avg_rating_180d,
            data.category_diversity_180d,
            data.ticket_count_90d,
            data.negative_ticket_rate_90d,
            data.avg_resolution_hours_90d,
            data.days_since_signup,
            data.sessions_30d,
            data.product_views_30d,
            data.cart_adds_30d,
            data.wishlist_adds_30d,
            data.abandoned_carts_30d,
            data.email_opens_30d,
            data.campaign_clicks_30d,
            data.last_visit_days_ago,
            data.city_tier_Tier_2,
            data.city_tier_Tier_3,
            data.age_group_25_34,
            data.age_group_35_44,
            data.age_group_45_plus,
            data.acquisition_channel_Influencer,
            data.acquisition_channel_Instagram,
            data.acquisition_channel_Marketplace,
            data.acquisition_channel_Organic,
            data.acquisition_channel_Referral,
            data.loyalty_tier_Platinum,
            data.loyalty_tier_Silver,
            data.preferred_category_Fragrance,
            data.preferred_category_Hair_Care,
            data.preferred_category_Makeup,
            data.preferred_category_Skin_Care,
            data.preferred_category_Wellness,
            data.marketing_consent_Yes
        ]]

        prediction = int(model.predict(features)[0])

        probability = float(model.predict_proba(features)[0][1])

        if probability >= 0.8:
            risk = "High churn risk"
        elif probability >= 0.5:
            risk = "Medium churn risk"
        else:
            risk = "Low churn risk"

        results.append({
            "churn_prediction": prediction,
            "churn_probability": round(probability, 4),
            "risk_explanation": risk
        })

    return {"predictions": results}