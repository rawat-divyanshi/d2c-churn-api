from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict():
    payload = {
        "recency_days": 30,
        "frequency_180d": 5,
        "monetary_180d": 500,
        "return_rate_180d": 0.1,
        "avg_discount_pct_180d": 10,
        "avg_rating_180d": 4.5,
        "category_diversity_180d": 3,
        "ticket_count_90d": 0,
        "negative_ticket_rate_90d": 0,
        "avg_resolution_hours_90d": 24,
        "days_since_signup": 365,
        "sessions_30d": 10,
        "product_views_30d": 20,
        "cart_adds_30d": 5,
        "wishlist_adds_30d": 2,
        "abandoned_carts_30d": 1,
        "email_opens_30d": 4,
        "campaign_clicks_30d": 1,
        "last_visit_days_ago": 7,
        "city_tier_Tier_2": 1,
        "city_tier_Tier_3": 0,
        "age_group_25_34": 1,
        "age_group_35_44": 0,
        "age_group_45_plus": 0,
        "acquisition_channel_Influencer": 0,
        "acquisition_channel_Instagram": 1,
        "acquisition_channel_Marketplace": 0,
        "acquisition_channel_Organic": 0,
        "acquisition_channel_Referral": 0,
        "loyalty_tier_Platinum": 0,
        "loyalty_tier_Silver": 1,
        "preferred_category_Fragrance": 0,
        "preferred_category_Hair_Care": 1,
        "preferred_category_Makeup": 0,
        "preferred_category_Skin_Care": 0,
        "preferred_category_Wellness": 0,
        "marketing_consent_Yes": 1
    }

    response = client.post("/predict", json=payload)

    print(response.json())

    assert response.status_code == 200
    assert "churn_prediction" in response.json()


def test_batch_predict():
    payload = [{
        "recency_days": 30,
        "frequency_180d": 5,
        "monetary_180d": 500,
        "return_rate_180d": 0.1,
        "avg_discount_pct_180d": 10,
        "avg_rating_180d": 4.5,
        "category_diversity_180d": 3,
        "ticket_count_90d": 0,
        "negative_ticket_rate_90d": 0,
        "avg_resolution_hours_90d": 24,
        "days_since_signup": 365,
        "sessions_30d": 10,
        "product_views_30d": 20,
        "cart_adds_30d": 5,
        "wishlist_adds_30d": 2,
        "abandoned_carts_30d": 1,
        "email_opens_30d": 4,
        "campaign_clicks_30d": 1,
        "last_visit_days_ago": 7,
        "city_tier_Tier_2": 1,
        "city_tier_Tier_3": 0,
        "age_group_25_34": 1,
        "age_group_35_44": 0,
        "age_group_45_plus": 0,
        "acquisition_channel_Influencer": 0,
        "acquisition_channel_Instagram": 1,
        "acquisition_channel_Marketplace": 0,
        "acquisition_channel_Organic": 0,
        "acquisition_channel_Referral": 0,
        "loyalty_tier_Platinum": 0,
        "loyalty_tier_Silver": 1,
        "preferred_category_Fragrance": 0,
        "preferred_category_Hair_Care": 1,
        "preferred_category_Makeup": 0,
        "preferred_category_Skin_Care": 0,
        "preferred_category_Wellness": 0,
        "marketing_consent_Yes": 1
    }]

    response = client.post("/batch_predict", json=payload)

    assert response.status_code == 200
    assert "predictions" in response.json()