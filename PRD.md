# Product Requirements Document (PRD)

**Product Name**: Food Market Platform
**Prepared by**: \[You]
**Date**: \[Insert Date]

---

## 1. Overview

The Food Market Platform is a web-based solution that enables users — especially elderly and mobility-limited individuals — to browse, compare, and purchase products from food markets without physically visiting them.

---

## 2. Goals & Objectives

* Accessibility-first design.
* Allow any food market to register and manage assortments.
* Enable seamless ordering with order comments.
* Provide an admin dashboard for monitoring statistics and managing inventory.
* Support English (default) and Ukrainian with i18next.

---

## 3. Target Users

* **Primary Users**: Elderly or mobility-limited individuals.
* **Secondary Users**: General consumers.
* **Admin Users**: Food market owners/managers.

---

## 4. Features

### 4.1 Customer-facing

* Browse assortments.
* Filter/search by category, tags, stock.
* Place orders with comments.
* View/manage order history.
* Customize font, font size, theme.
* Localization (EN/UA).

### 4.2 Admin-facing

* Manage assortments.
* Add/edit/remove product details.
* View incoming orders.
* Statistics dashboard.
* Role-based authentication.

---

## 5. Technical Requirements

### 5.1 Frontend

* React, ShadCN, React Query, TanStack Router, TailwindCSS.
* i18next for localization.
* TypeScript for type safety.
* Custom accessibility-first theme design.
* Modern, easy-to-use, non-eye-straining UI.

### 5.2 Backend

* FastAPI (Python).
* MongoDB (local development with production switch capability).
* JWT-based authentication (Clerk integration planned).
* Pydantic for schemas.
* Local file storage for images.

### 5.3 Documentation

* docsify-cli.
* Docker containerization with Docker Compose.
* Comprehensive deployment documentation.

### 5.4 Testing

* **TDD Approach**: Test-first development with full coverage.
* pytest for backend with comprehensive test cases.
* Jest/RTL for frontend with component testing.
* Integration testing with Playwright.
* Accessibility testing with automated tools.

---

## 6. Accessibility Requirements

* Adjustable font size.
* Font customization.
* Dark/Light mode with high contrast.

---

## 7. Localization Requirements

* Base language: English.
* Support for Ukrainian.
* `/translations/<lang>.json` based localization.

---

## 8. Non-Functional Requirements

* Performance: <200ms API responses.
* Scalability: Multiple markets.
* Security: JWT, hashed passwords.
* Reliability: 99.5% uptime.

---

## 9. Success Metrics

* Active users.
* Registered markets.
* Orders placed.
* User satisfaction feedback.
* Accessibility compliance.

---

## 10. Database Models & Schemas

The following are MongoDB collections with **Pydantic schemas** for FastAPI, and **TypeScript types** for frontend type safety.

### 10.1 User Model

```python
# backend/models/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional
from bson import ObjectId

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., max_length=100)
    role: Literal["customer", "market_admin", "super_admin"] = "customer"
    locale: Literal["en", "ua"] = "en"

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserInDB(UserBase):
    id: str
    hashed_password: str

class UserPublic(UserBase):
    id: str
```

**Frontend Type (TypeScript)**

```ts
// frontend/types/user.ts
export type UserRole = "customer" | "market_admin" | "super_admin";

export interface UserPublic {
  id: string;
  email: string;
  name: string;
  role: UserRole;
  locale: "en" | "ua";
}
```

---

### 10.2 Market Model

```python
# backend/models/market.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class MarketBase(BaseModel):
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    contact_email: EmailStr
    contact_phone: Optional[str] = None
    address: Optional[str] = None

class MarketCreate(MarketBase):
    owner_id: str

class MarketInDB(MarketBase):
    id: str
    owner_id: str

class MarketPublic(MarketBase):
    id: str
```

**Frontend Type (TypeScript)**

```ts
// frontend/types/market.ts
export interface MarketPublic {
  id: string;
  name: string;
  description?: string;
  contact_email: string;
  contact_phone?: string;
  address?: string;
}
```

---

### 10.3 Product Model

```python
# backend/models/product.py
from pydantic import BaseModel, Field
from typing import Optional, List

class ProductBase(BaseModel):
    market_id: str
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    price: float
    stock_quantity: int
    category: str
    sub_category: Optional[str] = None
    tags: List[str] = []
    images: List[str] = []

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: str

class ProductPublic(ProductBase):
    id: str
```

**Frontend Type (TypeScript)**

```ts
// frontend/types/product.ts
export interface ProductPublic {
  id: string;
  market_id: string;
  name: string;
  description?: string;
  price: number;
  stock_quantity: number;
  category: string;
  sub_category?: string;
  tags: string[];
  images: string[];
}
```

---

### 10.4 Order Model

```python
# backend/models/order.py
from pydantic import BaseModel, Field
from typing import List, Optional

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderBase(BaseModel):
    user_id: str
    market_id: str
    items: List[OrderItem]
    comment: Optional[str] = None
    status: str = Field(default="pending", regex="^(pending|confirmed|delivered|cancelled)$")

class OrderCreate(OrderBase):
    pass

class OrderInDB(OrderBase):
    id: str

class OrderPublic(OrderBase):
    id: str
```

**Frontend Type (TypeScript)**

```ts
// frontend/types/order.ts
export type OrderStatus = "pending" | "confirmed" | "delivered" | "cancelled";

export interface OrderItem {
  product_id: string;
  quantity: number;
}

export interface OrderPublic {
  id: string;
  user_id: string;
  market_id: string;
  items: OrderItem[];
  comment?: string;
  status: OrderStatus;
}
```

---

### 10.5 Statistics Model

```python
# backend/models/statistics.py
from pydantic import BaseModel

class ProductStats(BaseModel):
    product_id: str
    total_orders: int
    total_sold: int
    revenue: float

class MarketStats(BaseModel):
    market_id: str
    total_orders: int
    total_revenue: float
    top_products: list[ProductStats]
```

**Frontend Type (TypeScript)**

```ts
// frontend/types/statistics.ts
export interface ProductStats {
  product_id: string;
  total_orders: number;
  total_sold: number;
  revenue: number;
}

export interface MarketStats {
  market_id: string;
  total_orders: number;
  total_revenue: number;
  top_products: ProductStats[];
}
```

---

## 11. Data Relationships

* **User ↔ Market**: One user (market\_admin) owns a market.
* **Market ↔ Product**: One market has many products.
* **User ↔ Order**: One user can place multiple orders.
* **Order ↔ Product**: Many-to-many via `OrderItem`.
