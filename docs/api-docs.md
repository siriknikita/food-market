# API Documentation

## 🔗 API Overview

The Food Market Platform API is built with **FastAPI** and provides RESTful endpoints for all platform functionality. The API follows REST conventions and uses JSON for data exchange.

### Base URL

```text
Development: http://localhost:8000/api/v1
Production: https://api.foodmarket.com/api/v1
```

### Authentication

All API endpoints require authentication via JWT tokens obtained from Clerk authentication service.

```http
Authorization: Bearer <jwt_token>
```

---

## 📋 API Endpoints

### Authentication Endpoints

#### POST /auth/login

Authenticate user and return JWT token.

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "customer",
    "locale": "en"
  }
}
```

#### POST /auth/register

Register a new user account.

**Request Body:**

```json
{
  "email": "newuser@example.com",
  "name": "Jane Smith",
  "password": "securepassword123",
  "confirm_password": "securepassword123",
  "role": "customer",
  "locale": "en"
}
```

**Response:**

```json
{
  "message": "User registered successfully",
  "user": {
    "id": "user_id",
    "email": "newuser@example.com",
    "name": "Jane Smith",
    "role": "customer",
    "locale": "en"
  }
}
```

#### POST /auth/refresh

Refresh JWT token.

**Request Body:**

```json
{
  "refresh_token": "refresh_token_here"
}
```

**Response:**

```json
{
  "access_token": "new_jwt_token",
  "token_type": "bearer",
  "expires_in": 3600
}
```

---

### User Endpoints

#### GET /users/me

Get current user profile.

**Headers:**

```http
Authorization: Bearer <jwt_token>
```

**Response:**

```json
{
  "id": "user_id",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "customer",
  "locale": "en",
  "phone": "+1234567890",
  "address": "123 Main St, City, State",
  "preferences": {
    "fontSize": "medium",
    "theme": "light",
    "notifications": {
      "email": true,
      "push": false,
      "sms": false
    }
  },
  "created_at": "2024-01-15T10:30:00Z",
  "is_active": true
}
```

#### PUT /users/me

Update current user profile.

**Request Body:**

```json
{
  "name": "John Updated",
  "phone": "+1234567890",
  "address": "456 Oak St, City, State",
  "preferences": {
    "fontSize": "large",
    "theme": "dark",
    "notifications": {
      "email": true,
      "push": true,
      "sms": false
    }
  }
}
```

**Response:**

```json
{
  "message": "Profile updated successfully",
  "user": {
    "id": "user_id",
    "name": "John Updated",
    "phone": "+1234567890",
    "address": "456 Oak St, City, State",
    "preferences": {
      "fontSize": "large",
      "theme": "dark",
      "notifications": {
        "email": true,
        "push": true,
        "sms": false
      }
    }
  }
}
```

#### DELETE /users/me

Deactivate current user account.

**Response:**

```json
{
  "message": "Account deactivated successfully"
}
```

---

### Market Endpoints

#### GET /markets

Get list of available markets.

**Query Parameters:**

- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20)
- `verified` (bool): Filter by verification status
- `active` (bool): Filter by active status
- `search` (string): Search by market name

**Response:**

```json
{
  "markets": [
    {
      "id": "market_id",
      "name": "Fresh Market",
      "description": "Local fresh produce market",
      "contact_email": "contact@freshmarket.com",
      "contact_phone": "+1234567890",
      "address": "123 Main St, City, State",
      "coordinates": {
        "lat": 40.7128,
        "lng": -74.0060
      },
      "business_hours": {
        "monday": {"open": "09:00", "close": "18:00"},
        "tuesday": {"open": "09:00", "close": "18:00"}
      },
      "delivery_options": ["pickup", "delivery"],
      "payment_methods": ["cash", "card"],
      "is_active": true,
      "verified": true,
      "rating": 4.5,
      "total_orders": 150,
      "total_revenue": 15000.00
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 50,
    "pages": 3
  }
}
```

#### GET /markets/{market_id}

Get specific market details.

**Response:**

```json
{
  "id": "market_id",
  "name": "Fresh Market",
  "description": "Local fresh produce market",
  "contact_email": "contact@freshmarket.com",
  "contact_phone": "+1234567890",
  "address": "123 Main St, City, State",
  "coordinates": {
    "lat": 40.7128,
    "lng": -74.0060
  },
  "business_hours": {
    "monday": {"open": "09:00", "close": "18:00"},
    "tuesday": {"open": "09:00", "close": "18:00"},
    "wednesday": {"open": "09:00", "close": "18:00"},
    "thursday": {"open": "09:00", "close": "18:00"},
    "friday": {"open": "09:00", "close": "18:00"},
    "saturday": {"open": "09:00", "close": "17:00"},
    "sunday": {"open": "10:00", "close": "16:00"}
  },
  "delivery_options": ["pickup", "delivery"],
  "payment_methods": ["cash", "card"],
  "is_active": true,
  "owner_id": "owner_id",
  "created_at": "2024-01-01T00:00:00Z",
  "verified": true,
  "rating": 4.5,
  "total_orders": 150,
  "total_revenue": 15000.00
}
```

#### POST /markets

Create a new market (Market Admin only).

**Request Body:**

```json
{
  "name": "New Market",
  "description": "A new local market",
  "contact_email": "contact@newmarket.com",
  "contact_phone": "+1234567890",
  "address": "789 Pine St, City, State",
  "coordinates": {
    "lat": 40.7128,
    "lng": -74.0060
  },
  "business_hours": {
    "monday": {"open": "09:00", "close": "18:00"},
    "tuesday": {"open": "09:00", "close": "18:00"}
  },
  "delivery_options": ["pickup"],
  "payment_methods": ["cash", "card"]
}
```

**Response:**

```json
{
  "message": "Market created successfully",
  "market": {
    "id": "new_market_id",
    "name": "New Market",
    "description": "A new local market",
    "contact_email": "contact@newmarket.com",
    "contact_phone": "+1234567890",
    "address": "789 Pine St, City, State",
    "is_active": true,
    "verified": false
  }
}
```

#### PUT /markets/{market_id}

Update market details (Market Admin only).

**Request Body:**

```json
{
  "name": "Updated Market Name",
  "description": "Updated description",
  "contact_phone": "+1987654321",
  "business_hours": {
    "monday": {"open": "08:00", "close": "19:00"}
  }
}
```

**Response:**

```json
{
  "message": "Market updated successfully",
  "market": {
    "id": "market_id",
    "name": "Updated Market Name",
    "description": "Updated description",
    "contact_phone": "+1987654321"
  }
}
```

---

### Product Endpoints

#### GET /markets/{market_id}/products

Get products for a specific market.

**Query Parameters:**

- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20)
- `category` (string): Filter by category
- `sub_category` (string): Filter by sub-category
- `search` (string): Search by product name
- `min_price` (float): Minimum price filter
- `max_price` (float): Maximum price filter
- `in_stock` (bool): Filter by stock availability
- `featured` (bool): Filter featured products

**Response:**

```json
{
  "products": [
    {
      "id": "product_id",
      "market_id": "market_id",
      "name": "Fresh Apples",
      "description": "Organic red apples",
      "price": 2.99,
      "stock_quantity": 100,
      "category": "fruits",
      "sub_category": "apples",
      "tags": ["organic", "fresh", "local"],
      "images": ["https://example.com/apple1.jpg"],
      "unit": "kg",
      "weight": 150.0,
      "dimensions": {
        "length": 8.0,
        "width": 6.0,
        "height": 2.0
      },
      "is_active": true,
      "featured": false,
      "total_sold": 50,
      "total_revenue": 149.50,
      "rating": 4.2,
      "review_count": 12
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

#### GET /products/{product_id}

Get specific product details.

**Response:**

```json
{
  "id": "product_id",
  "market_id": "market_id",
  "name": "Fresh Apples",
  "description": "Organic red apples from local farms",
  "price": 2.99,
  "stock_quantity": 100,
  "category": "fruits",
  "sub_category": "apples",
  "tags": ["organic", "fresh", "local", "seasonal"],
  "images": [
    "https://example.com/apple1.jpg",
    "https://example.com/apple2.jpg"
  ],
  "unit": "kg",
  "weight": 150.0,
  "dimensions": {
    "length": 8.0,
    "width": 6.0,
    "height": 2.0
  },
  "is_active": true,
  "featured": false,
  "created_at": "2024-01-01T00:00:00Z",
  "total_sold": 50,
  "total_revenue": 149.50,
  "rating": 4.2,
  "review_count": 12
}
```

#### POST /markets/{market_id}/products

Create a new product (Market Admin only).

**Request Body:**

```json
{
  "name": "Fresh Oranges",
  "description": "Sweet and juicy oranges",
  "price": 3.49,
  "stock_quantity": 75,
  "category": "fruits",
  "sub_category": "citrus",
  "tags": ["organic", "fresh"],
  "images": ["https://example.com/orange1.jpg"],
  "unit": "kg",
  "weight": 200.0,
  "featured": false
}
```

**Response:**

```json
{
  "message": "Product created successfully",
  "product": {
    "id": "new_product_id",
    "name": "Fresh Oranges",
    "description": "Sweet and juicy oranges",
    "price": 3.49,
    "stock_quantity": 75,
    "category": "fruits",
    "sub_category": "citrus",
    "is_active": true,
    "featured": false
  }
}
```

#### PUT /products/{product_id}

Update product details (Market Admin only).

**Request Body:**

```json
{
  "name": "Updated Product Name",
  "description": "Updated description",
  "price": 3.99,
  "stock_quantity": 80,
  "featured": true
}
```

**Response:**

```json
{
  "message": "Product updated successfully",
  "product": {
    "id": "product_id",
    "name": "Updated Product Name",
    "description": "Updated description",
    "price": 3.99,
    "stock_quantity": 80,
    "featured": true
  }
}
```

#### DELETE /products/{product_id}

Deactivate product (Market Admin only).

**Response:**

```json
{
  "message": "Product deactivated successfully"
}
```

---

### Order Endpoints

#### GET /orders

Get user's order history.

**Query Parameters:**

- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20)
- `status` (string): Filter by order status
- `market_id` (string): Filter by market

**Response:**

```json
{
  "orders": [
    {
      "id": "order_id",
      "order_number": "ORD-2024-001",
      "user_id": "user_id",
      "market_id": "market_id",
      "items": [
        {
          "product_id": "product_id",
          "quantity": 2,
          "unit_price": 2.99,
          "total_price": 5.98
        }
      ],
      "comment": "Please pack carefully",
      "status": "confirmed",
      "delivery_option": "pickup",
      "delivery_address": null,
      "delivery_time": null,
      "total_amount": 5.98,
      "tax_amount": 0.00,
      "discount_amount": 0.00,
      "final_amount": 5.98,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:35:00Z",
      "confirmed_at": "2024-01-15T10:35:00Z",
      "payment_status": "paid",
      "payment_method": "card",
      "estimated_delivery": "2024-01-15T14:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 25,
    "pages": 2
  }
}
```

#### GET /orders/{order_id}

Get specific order details.

**Response:**

```json
{
  "id": "order_id",
  "order_number": "ORD-2024-001",
  "user_id": "user_id",
  "market_id": "market_id",
  "items": [
    {
      "product_id": "product_id",
      "product_name": "Fresh Apples",
      "quantity": 2,
      "unit_price": 2.99,
      "total_price": 5.98
    }
  ],
  "comment": "Please pack carefully",
  "status": "confirmed",
  "delivery_option": "pickup",
  "delivery_address": null,
  "delivery_time": null,
  "total_amount": 5.98,
  "tax_amount": 0.00,
  "discount_amount": 0.00,
  "final_amount": 5.98,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:35:00Z",
  "confirmed_at": "2024-01-15T10:35:00Z",
  "prepared_at": null,
  "ready_at": null,
  "delivered_at": null,
  "cancelled_at": null,
  "cancelled_reason": null,
  "payment_status": "paid",
  "payment_method": "card",
  "estimated_delivery": "2024-01-15T14:00:00Z"
}
```

#### POST /orders

Create a new order.

**Request Body:**

```json
{
  "market_id": "market_id",
  "items": [
    {
      "product_id": "product_id",
      "quantity": 2
    }
  ],
  "comment": "Please pack carefully",
  "delivery_option": "pickup",
  "delivery_address": null,
  "delivery_time": null
}
```

**Response:**

```json
{
  "message": "Order created successfully",
  "order": {
    "id": "order_id",
    "order_number": "ORD-2024-002",
    "user_id": "user_id",
    "market_id": "market_id",
    "items": [
      {
        "product_id": "product_id",
        "quantity": 2,
        "unit_price": 2.99,
        "total_price": 5.98
      }
    ],
    "comment": "Please pack carefully",
    "status": "pending",
    "delivery_option": "pickup",
    "total_amount": 5.98,
    "final_amount": 5.98,
    "created_at": "2024-01-15T11:00:00Z"
  }
}
```

#### PUT /orders/{order_id}/cancel

Cancel an order.

**Request Body:**

```json
{
  "reason": "Changed my mind"
}
```

**Response:**

```json
{
  "message": "Order cancelled successfully",
  "order": {
    "id": "order_id",
    "status": "cancelled",
    "cancelled_at": "2024-01-15T11:30:00Z",
    "cancelled_reason": "Changed my mind"
  }
}
```

---

### Admin Order Management Endpoints

#### GET /admin/orders

Get all orders for market admin.

**Query Parameters:**

- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20)
- `status` (string): Filter by order status
- `date_from` (string): Filter from date (YYYY-MM-DD)
- `date_to` (string): Filter to date (YYYY-MM-DD)

**Response:**

```json
{
  "orders": [
    {
      "id": "order_id",
      "order_number": "ORD-2024-001",
      "user": {
        "id": "user_id",
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "+1234567890"
      },
      "items": [
        {
          "product_id": "product_id",
          "product_name": "Fresh Apples",
          "quantity": 2,
          "unit_price": 2.99,
          "total_price": 5.98
        }
      ],
      "status": "pending",
      "delivery_option": "pickup",
      "total_amount": 5.98,
      "final_amount": 5.98,
      "created_at": "2024-01-15T10:30:00Z",
      "payment_status": "pending"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

#### PUT /admin/orders/{order_id}/status

Update order status (Market Admin only).

**Request Body:**

```json
{
  "status": "confirmed"
}
```

**Response:**

```json
{
  "message": "Order status updated successfully",
  "order": {
    "id": "order_id",
    "status": "confirmed",
    "confirmed_at": "2024-01-15T12:00:00Z"
  }
}
```

---

### Analytics Endpoints

#### GET /admin/analytics/market

Get market analytics (Market Admin only).

**Query Parameters:**

- `period` (string): Time period (day, week, month, year)
- `date_from` (string): Start date (YYYY-MM-DD)
- `date_to` (string): End date (YYYY-MM-DD)

**Response:**

```json
{
  "market_id": "market_id",
  "market_name": "Fresh Market",
  "total_orders": 150,
  "total_revenue": 15000.00,
  "total_customers": 75,
  "average_order_value": 100.00,
  "top_products": [
    {
      "product_id": "product_id",
      "product_name": "Fresh Apples",
      "total_orders": 25,
      "total_sold": 50,
      "revenue": 149.50,
      "average_rating": 4.2,
      "review_count": 12
    }
  ],
  "order_status_distribution": {
    "pending": 10,
    "confirmed": 20,
    "preparing": 15,
    "ready": 5,
    "delivered": 100
  },
  "daily_sales": [
    {
      "date": "2024-01-15",
      "revenue": 500.00,
      "orders": 5
    }
  ],
  "monthly_sales": [
    {
      "month": "2024-01",
      "revenue": 15000.00,
      "orders": 150
    }
  ]
}
```

#### GET /admin/analytics/platform

Get platform analytics (Super Admin only).

**Response:**

```json
{
  "total_users": 1000,
  "total_markets": 50,
  "total_products": 5000,
  "total_orders": 5000,
  "total_revenue": 500000.00,
  "active_markets": 45,
  "active_users": 800,
  "average_order_value": 100.00,
  "top_markets": [
    {
      "market_id": "market_id",
      "market_name": "Fresh Market",
      "total_orders": 150,
      "total_revenue": 15000.00,
      "total_customers": 75,
      "average_order_value": 100.00
    }
  ],
  "system_health": {
    "uptime": 99.9,
    "response_time": 150,
    "error_rate": 0.1
  },
  "performance_metrics": {
    "api_requests_per_minute": 1000,
    "database_connections": 50,
    "cache_hit_rate": 85.5
  }
}
```

---

## 🔒 Error Handling

### Error Response Format

All API errors follow a consistent format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

### Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `VALIDATION_ERROR` | 400 | Request validation failed |
| `UNAUTHORIZED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `CONFLICT` | 409 | Resource conflict |
| `RATE_LIMITED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server error |

### Example Error Responses

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required",
    "details": []
  }
}
```

#### 403 Forbidden

```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "Insufficient permissions to access this resource",
    "details": []
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Product not found",
    "details": [
      {
        "field": "product_id",
        "message": "Product with ID 'invalid_id' does not exist"
      }
    ]
  }
}
```

#### 429 Rate Limited

```json
{
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests. Please try again later.",
    "details": [
      {
        "field": "rate_limit",
        "message": "Rate limit: 100 requests per minute"
      }
    ]
  }
}
```

---

## 📊 Rate Limiting

### Rate Limit Rules

- **Authentication endpoints**: 5 requests per minute
- **User endpoints**: 100 requests per minute
- **Market endpoints**: 200 requests per minute
- **Product endpoints**: 300 requests per minute
- **Order endpoints**: 50 requests per minute
- **Analytics endpoints**: 20 requests per minute

### Rate Limit Headers

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642248600
```

---

## 🔄 Webhooks

### Webhook Events

The API supports webhooks for real-time notifications:

#### Order Events

- `order.created` - New order placed
- `order.updated` - Order status changed
- `order.cancelled` - Order cancelled

#### Product Events

- `product.created` - New product added
- `product.updated` - Product updated
- `product.deactivated` - Product deactivated

### Webhook Payload Example

```json
{
  "event": "order.created",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    "order_id": "order_id",
    "order_number": "ORD-2024-001",
    "market_id": "market_id",
    "user_id": "user_id",
    "status": "pending",
    "total_amount": 5.98
  }
}
```

---

## 📚 SDKs & Libraries

### JavaScript/TypeScript SDK

```javascript
import { FoodMarketAPI } from '@foodmarket/sdk';

const api = new FoodMarketAPI({
  baseURL: 'https://api.foodmarket.com/api/v1',
  token: 'your_jwt_token'
});

// Get markets
const markets = await api.markets.list();

// Create order
const order = await api.orders.create({
  market_id: 'market_id',
  items: [{ product_id: 'product_id', quantity: 2 }]
});
```

### Python SDK

```python
from foodmarket_sdk import FoodMarketAPI

api = FoodMarketAPI(
    base_url="https://api.foodmarket.com/api/v1",
    token="your_jwt_token"
)

# Get markets
markets = api.markets.list()

# Create order
order = api.orders.create({
    "market_id": "market_id",
    "items": [{"product_id": "product_id", "quantity": 2}]
})
```

---

## 🧪 Testing

### API Testing with Postman

Import the following collection for testing:

```json
{
  "info": {
    "name": "Food Market API",
    "description": "Complete API collection for Food Market Platform"
  },
  "item": [
    {
      "name": "Authentication",
      "item": [
        {
          "name": "Login",
          "request": {
            "method": "POST",
            "url": "{{base_url}}/auth/login",
            "body": {
              "mode": "raw",
              "raw": "{\"email\":\"user@example.com\",\"password\":\"password\"}",
              "options": {
                "raw": {
                  "language": "json"
                }
              }
            }
          }
        }
      ]
    }
  ]
}
```

### Environment Variables

```bash
# Development
base_url=http://localhost:8000/api/v1
jwt_token=your_development_token

# Production
base_url=https://api.foodmarket.com/api/v1
jwt_token=your_production_token
```
