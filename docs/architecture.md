# System Architecture

## 🏗️ Architecture Overview

The Food Market Platform follows a **modern microservices-inspired architecture** with clear separation of concerns, scalability, and maintainability as primary design principles.

### High-Level Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[React SPA] --> B[TanStack Router]
        B --> C[React Query]
        C --> D[ShadCN UI Components]
        D --> E[TailwindCSS]
    end
    
    subgraph "API Gateway"
        F[FastAPI Gateway] --> G[Authentication]
        F --> H[Rate Limiting]
        F --> I[Request Validation]
    end
    
    subgraph "Backend Services"
        J[User Service] --> K[MongoDB Users]
        L[Market Service] --> M[MongoDB Markets]
        N[Product Service] --> O[MongoDB Products]
        P[Order Service] --> Q[MongoDB Orders]
        R[Analytics Service] --> S[MongoDB Statistics]
    end
    
    subgraph "External Services"
        T[Clerk Auth] --> U[JWT Tokens]
        V[File Storage] --> W[Product Images]
        X[Email Service] --> Y[Notifications]
    end
    
    A --> F
    F --> J
    F --> L
    F --> N
    F --> P
    F --> R
    J --> T
    N --> V
    P --> X
```

---

## 🎯 Design Principles

### 1. Accessibility First

- **Universal Design**: Interfaces work for users of all abilities
- **Progressive Enhancement**: Core functionality without JavaScript
- **Semantic HTML**: Proper markup for screen readers
- **Keyboard Navigation**: Full keyboard accessibility

### 2. Performance Optimization

- **<200ms API Response**: Fast backend processing
- **Lazy Loading**: Images and components loaded on demand
- **Caching Strategy**: Redis for frequently accessed data
- **CDN Integration**: Static assets delivery optimization

### 3. Security by Design

- **JWT Authentication**: Secure token-based authentication
- **Input Validation**: Pydantic schemas for data integrity
- **Rate Limiting**: API abuse prevention
- **HTTPS Enforcement**: Secure communication protocols

### 4. Scalability

- **Horizontal Scaling**: Stateless services for easy scaling
- **Database Indexing**: Optimized query performance
- **Microservices Ready**: Service decomposition for growth
- **Load Balancing**: Traffic distribution across instances

---

## 🏛️ System Components

### Frontend Architecture

```mermaid
graph LR
    subgraph "React Application"
        A[App Component] --> B[Router]
        B --> C[Pages]
        C --> D[Components]
        D --> E[Hooks]
        E --> F[Services]
    end
    
    subgraph "State Management"
        G[React Query] --> H[Server State]
        I[Context API] --> J[Client State]
        K[Local Storage] --> L[User Preferences]
    end
    
    subgraph "UI Framework"
        M[ShadCN UI] --> N[Custom Components]
        O[TailwindCSS] --> P[Styling]
        Q[i18next] --> R[Localization]
    end
    
    F --> G
    F --> I
    F --> K
    D --> M
    D --> O
    D --> Q
```

#### Component Hierarchy

```text
App/
├── Layout/
│   ├── Header/
│   │   ├── Navigation
│   │   ├── UserMenu
│   │   └── AccessibilityControls
│   ├── Sidebar/
│   │   ├── MarketList
│   │   └── CategoryFilter
│   └── Footer/
├── Pages/
│   ├── Home/
│   ├── Markets/
│   ├── Products/
│   ├── Cart/
│   ├── Orders/
│   └── Admin/
├── Components/
│   ├── Common/
│   │   ├── Button
│   │   ├── Input
│   │   ├── Modal
│   │   └── Loading
│   ├── Product/
│   │   ├── ProductCard
│   │   ├── ProductList
│   │   └── ProductDetail
│   └── Order/
│       ├── OrderSummary
│       ├── OrderHistory
│       └── OrderStatus
└── Hooks/
    ├── useAuth
    ├── useCart
    ├── useOrders
    └── useMarkets
```

### Backend Architecture

```mermaid
graph TB
    subgraph "FastAPI Application"
        A[Main App] --> B[Middleware]
        B --> C[Authentication]
        C --> D[Rate Limiting]
        D --> E[Request Validation]
        E --> F[Error Handling]
    end
    
    subgraph "API Routes"
        G[User Routes] --> H[User Service]
        I[Market Routes] --> J[Market Service]
        K[Product Routes] --> L[Product Service]
        M[Order Routes] --> N[Order Service]
        O[Analytics Routes] --> P[Analytics Service]
    end
    
    subgraph "Data Layer"
        Q[MongoDB] --> R[Users Collection]
        Q --> S[Markets Collection]
        Q --> T[Products Collection]
        Q --> U[Orders Collection]
        Q --> V[Statistics Collection]
    end
    
    subgraph "External Services"
        W[Clerk Auth] --> X[JWT Validation]
        Y[File Storage] --> Z[Image Management]
        AA[Email Service] --> BB[Notifications]
    end
    
    F --> G
    F --> I
    F --> K
    F --> M
    F --> O
    H --> Q
    J --> Q
    L --> Q
    N --> Q
    P --> Q
    C --> W
    L --> Y
    N --> AA
```

#### Service Structure

```text
backend/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── config.py              # Configuration management
│   ├── dependencies.py        # Dependency injection
│   ├── middleware/
│   │   ├── auth.py           # Authentication middleware
│   │   ├── cors.py           # CORS configuration
│   │   ├── rate_limit.py     # Rate limiting
│   │   └── logging.py        # Request logging
│   ├── models/
│   │   ├── user.py           # User data models
│   │   ├── market.py         # Market data models
│   │   ├── product.py        # Product data models
│   │   ├── order.py          # Order data models
│   │   └── statistics.py     # Statistics models
│   ├── services/
│   │   ├── user_service.py   # User business logic
│   │   ├── market_service.py # Market business logic
│   │   ├── product_service.py # Product business logic
│   │   ├── order_service.py  # Order business logic
│   │   └── analytics_service.py # Analytics logic
│   ├── api/
│   │   ├── v1/
│   │   │   ├── users.py      # User endpoints
│   │   │   ├── markets.py    # Market endpoints
│   │   │   ├── products.py   # Product endpoints
│   │   │   ├── orders.py     # Order endpoints
│   │   │   └── analytics.py  # Analytics endpoints
│   │   └── deps.py           # API dependencies
│   ├── core/
│   │   ├── security.py       # Security utilities
│   │   ├── database.py       # Database connection
│   │   └── exceptions.py     # Custom exceptions
│   └── utils/
│       ├── validators.py     # Custom validators
│       ├── helpers.py        # Utility functions
│       └── constants.py      # Application constants
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── migrations/
├── requirements.txt
└── Dockerfile
```

---

## 🔄 Data Flow Architecture

### Request Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant G as API Gateway
    participant A as Auth Service
    participant S as Backend Service
    participant D as Database
    participant E as External Service

    U->>F: User Action
    F->>G: API Request
    G->>A: Validate Token
    A-->>G: Token Valid
    G->>S: Process Request
    S->>D: Database Query
    D-->>S: Query Result
    S->>E: External API Call (if needed)
    E-->>S: External Response
    S-->>G: Processed Response
    G-->>F: API Response
    F-->>U: UI Update
```

### Authentication Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant C as Clerk
    participant G as API Gateway
    participant S as Backend Service

    U->>F: Login Request
    F->>C: Authenticate User
    C-->>F: JWT Token
    F->>G: API Request with Token
    G->>S: Validate Token
    S-->>G: User Data
    G-->>F: Authenticated Response
    F-->>U: Logged In State
```

### Order Processing Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant G as API Gateway
    participant O as Order Service
    participant P as Product Service
    participant M as Market Service
    participant D as Database
    participant E as Email Service

    U->>F: Place Order
    F->>G: Create Order Request
    G->>O: Process Order
    O->>P: Check Inventory
    P-->>O: Inventory Status
    O->>D: Save Order
    D-->>O: Order Confirmed
    O->>M: Notify Market
    O->>E: Send Confirmation Email
    O-->>G: Order Response
    G-->>F: Order Confirmation
    F-->>U: Order Status Update
```

---

## 🗄️ Database Architecture

### MongoDB Collections Design

```mermaid
erDiagram
    USERS {
        ObjectId _id PK
        string email UK
        string name
        string role
        string locale
        string hashed_password
        datetime created_at
        datetime updated_at
        boolean is_active
        boolean email_verified
        datetime last_login
        object preferences
    }
    
    MARKETS {
        ObjectId _id PK
        string name
        string description
        string contact_email
        string contact_phone
        string address
        object coordinates
        object business_hours
        array delivery_options
        array payment_methods
        ObjectId owner_id FK
        datetime created_at
        datetime updated_at
        boolean verified
        float rating
        int total_orders
        float total_revenue
    }
    
    PRODUCTS {
        ObjectId _id PK
        ObjectId market_id FK
        string name
        string description
        decimal price
        int stock_quantity
        string category
        string sub_category
        array tags
        array images
        string unit
        float weight
        object dimensions
        boolean is_active
        boolean featured
        datetime created_at
        datetime updated_at
        int total_sold
        decimal total_revenue
        float rating
        int review_count
    }
    
    ORDERS {
        ObjectId _id PK
        string order_number UK
        ObjectId user_id FK
        ObjectId market_id FK
        array items
        string comment
        string status
        string delivery_option
        string delivery_address
        datetime delivery_time
        decimal total_amount
        decimal tax_amount
        decimal discount_amount
        decimal final_amount
        datetime created_at
        datetime updated_at
        datetime confirmed_at
        datetime prepared_at
        datetime ready_at
        datetime delivered_at
        datetime cancelled_at
        string cancelled_reason
        string payment_status
        string payment_method
        datetime estimated_delivery
    }
    
    STATISTICS {
        ObjectId _id PK
        string type
        ObjectId entity_id
        object data
        datetime created_at
        datetime updated_at
    }
    
    USERS ||--o{ MARKETS : "owns"
    MARKETS ||--o{ PRODUCTS : "has"
    USERS ||--o{ ORDERS : "places"
    MARKETS ||--o{ ORDERS : "receives"
    PRODUCTS ||--o{ ORDERS : "included_in"
```

### Indexing Strategy

#### Primary Indexes

```javascript
// Users collection
db.users.createIndex({ "email": 1 }, { unique: true })
db.users.createIndex({ "role": 1 })
db.users.createIndex({ "is_active": 1 })
db.users.createIndex({ "created_at": -1 })

// Markets collection
db.markets.createIndex({ "owner_id": 1 })
db.markets.createIndex({ "is_active": 1 })
db.markets.createIndex({ "verified": 1 })
db.markets.createIndex({ "coordinates": "2dsphere" })
db.markets.createIndex({ "created_at": -1 })

// Products collection
db.products.createIndex({ "market_id": 1 })
db.products.createIndex({ "category": 1 })
db.products.createIndex({ "is_active": 1 })
db.products.createIndex({ "featured": 1 })
db.products.createIndex({ "name": "text", "description": "text" })
db.products.createIndex({ "created_at": -1 })

// Orders collection
db.orders.createIndex({ "user_id": 1 })
db.orders.createIndex({ "market_id": 1 })
db.orders.createIndex({ "status": 1 })
db.orders.createIndex({ "created_at": -1 })
db.orders.createIndex({ "order_number": 1 }, { unique: true })
db.orders.createIndex({ "payment_status": 1 })
```

#### Compound Indexes

```javascript
// Market products by category and status
db.products.createIndex({ "market_id": 1, "category": 1, "is_active": 1 })

// User orders by status and date
db.orders.createIndex({ "user_id": 1, "status": 1, "created_at": -1 })

// Market orders by status and date
db.orders.createIndex({ "market_id": 1, "status": 1, "created_at": -1 })

// Product search optimization
db.products.createIndex({ "market_id": 1, "name": "text", "tags": 1 })
```

---

## 🔒 Security Architecture

### Authentication & Authorization

```mermaid
graph TB
    subgraph "Authentication Flow"
        A[User Login] --> B[Clerk Authentication]
        B --> C[JWT Token Generation]
        C --> D[Token Storage]
        D --> E[Token Validation]
    end
    
    subgraph "Authorization Layers"
        F[API Gateway] --> G[Token Validation]
        G --> H[Role Verification]
        H --> I[Permission Check]
        I --> J[Resource Access]
    end
    
    subgraph "Security Measures"
        K[Rate Limiting] --> L[Request Throttling]
        M[Input Validation] --> N[Data Sanitization]
        O[HTTPS Enforcement] --> P[Secure Communication]
        Q[Audit Logging] --> R[Security Monitoring]
    end
    
    E --> F
    J --> K
    J --> M
    J --> O
    J --> Q
```

### Security Components

#### 1. Authentication Service

- **Clerk Integration**: Third-party authentication provider
- **JWT Tokens**: Secure session management
- **Token Refresh**: Automatic token renewal
- **Multi-factor Authentication**: Enhanced security

#### 2. Authorization System

- **Role-based Access Control (RBAC)**: User, Market Admin, Super Admin
- **Permission Matrix**: Granular access control
- **Resource-level Security**: Individual resource protection
- **Session Management**: Secure session handling

#### 3. Data Protection

- **Input Validation**: Pydantic schemas for data integrity
- **SQL Injection Prevention**: Parameterized queries
- **XSS Protection**: Content Security Policy
- **CSRF Protection**: Cross-site request forgery prevention

#### 4. Network Security

- **HTTPS Enforcement**: TLS/SSL encryption
- **CORS Configuration**: Cross-origin resource sharing
- **Rate Limiting**: API abuse prevention
- **DDoS Protection**: Distributed denial of service mitigation

---

## 📊 Performance Architecture

### Caching Strategy

```mermaid
graph LR
    subgraph "Frontend Caching"
        A[React Query] --> B[Server State Cache]
        C[Local Storage] --> D[User Preferences]
        E[Session Storage] --> F[Temporary Data]
    end
    
    subgraph "Backend Caching"
        G[Redis Cache] --> H[Frequently Accessed Data]
        I[Database Query Cache] --> J[Optimized Queries]
        K[Static Asset Cache] --> L[CDN Distribution]
    end
    
    subgraph "Cache Invalidation"
        M[Cache Keys] --> N[TTL Management]
        O[Event-driven Invalidation] --> P[Data Consistency]
    end
    
    B --> G
    D --> G
    H --> I
    L --> K
    N --> M
    P --> O
```

### Performance Optimization

#### 1. Frontend Optimization

- **Code Splitting**: Lazy loading of components
- **Bundle Optimization**: Tree shaking and minification
- **Image Optimization**: WebP format and lazy loading
- **Service Workers**: Offline functionality

#### 2. Backend Optimization

- **Database Indexing**: Optimized query performance
- **Connection Pooling**: Efficient database connections
- **Async Processing**: Non-blocking operations
- **Compression**: Gzip response compression

#### 3. Network Optimization

- **CDN Integration**: Global content delivery
- **HTTP/2 Support**: Multiplexed connections
- **Resource Hints**: Preload and prefetch
- **Compression**: Response size reduction

---

## 🚀 Deployment Architecture

### Container Architecture

```mermaid
graph TB
    subgraph "Docker Containers"
        A[Frontend Container] --> B[Nginx Reverse Proxy]
        C[Backend Container] --> D[FastAPI Application]
        E[Database Container] --> F[MongoDB Instance]
        G[Redis Container] --> H[Cache Layer]
    end
    
    subgraph "Docker Compose"
        I[Compose File] --> J[Service Orchestration]
        K[Environment Variables] --> L[Configuration Management]
        M[Volume Mounts] --> N[Data Persistence]
    end
    
    subgraph "Production Deployment"
        O[Load Balancer] --> P[Multiple Instances]
        Q[SSL Termination] --> R[HTTPS Enforcement]
        S[Monitoring] --> T[Health Checks]
    end
    
    B --> D
    D --> F
    D --> H
    J --> A
    J --> C
    J --> E
    J --> G
    P --> B
    P --> D
    R --> Q
    T --> S
```

### Deployment Strategy

#### 1. Development Environment

- **Local Development**: Docker Compose for local setup
- **Hot Reloading**: Automatic code reloading
- **Debug Tools**: Development debugging utilities
- **Mock Services**: Simulated external services

#### 2. Staging Environment

- **Production-like**: Mirrors production configuration
- **Testing Ground**: Integration and E2E testing
- **Performance Testing**: Load and stress testing
- **Security Testing**: Vulnerability assessment

#### 3. Production Environment

- **High Availability**: Multiple instance deployment
- **Auto-scaling**: Dynamic resource allocation
- **Monitoring**: Real-time system monitoring
- **Backup Strategy**: Automated data backup

---

## 🔍 Monitoring & Observability

### Monitoring Architecture

```mermaid
graph TB
    subgraph "Application Monitoring"
        A[Application Metrics] --> B[Performance Data]
        C[Error Tracking] --> D[Exception Monitoring]
        E[User Analytics] --> F[Usage Statistics]
    end
    
    subgraph "Infrastructure Monitoring"
        G[System Metrics] --> H[Resource Utilization]
        I[Database Monitoring] --> J[Query Performance]
        K[Network Monitoring] --> L[Traffic Analysis]
    end
    
    subgraph "Alerting System"
        M[Threshold Alerts] --> N[Performance Degradation]
        O[Error Alerts] --> P[System Failures]
        Q[Capacity Alerts] --> R[Resource Exhaustion]
    end
    
    B --> M
    D --> O
    F --> M
    H --> Q
    J --> N
    L --> P
```

### Monitoring Components

#### 1. Application Performance Monitoring (APM)

- **Response Time Tracking**: API endpoint performance
- **Error Rate Monitoring**: Exception tracking
- **User Experience Metrics**: Frontend performance
- **Business Metrics**: Order completion rates

#### 2. Infrastructure Monitoring

- **Server Metrics**: CPU, memory, disk usage
- **Database Performance**: Query execution times
- **Network Monitoring**: Bandwidth and latency
- **Container Health**: Docker container status

#### 3. Logging & Tracing

- **Structured Logging**: JSON format logs
- **Distributed Tracing**: Request flow tracking
- **Audit Logging**: Security event logging
- **Error Logging**: Exception details

#### 4. Alerting & Notification

- **Threshold-based Alerts**: Performance degradation
- **Anomaly Detection**: Unusual system behavior
- **Escalation Procedures**: Alert routing
- **Notification Channels**: Email, Slack, SMS

---

## 🔄 CI/CD Pipeline

### Deployment Pipeline

```mermaid
graph LR
    A[Code Commit] --> B[GitHub Actions]
    B --> C[Code Quality Checks]
    C --> D[Unit Tests]
    D --> E[Integration Tests]
    E --> F[Security Scan]
    F --> G[Build Artifacts]
    G --> H[Deploy to Staging]
    H --> I[E2E Tests]
    I --> J[Deploy to Production]
    J --> K[Health Checks]
    K --> L[Monitoring]
```

### Pipeline Stages

#### 1. Code Quality

- **Linting**: Code style enforcement
- **Type Checking**: TypeScript validation
- **Security Scanning**: Vulnerability detection
- **Code Coverage**: Test coverage reporting

#### 2. Testing

- **Unit Tests**: Individual component testing
- **Integration Tests**: Service interaction testing
- **E2E Tests**: Full user journey testing
- **Performance Tests**: Load and stress testing

#### 3. Deployment

- **Staging Deployment**: Pre-production testing
- **Production Deployment**: Live environment update
- **Rollback Strategy**: Quick recovery procedures
- **Blue-Green Deployment**: Zero-downtime updates

---

## 📈 Scalability Considerations

### Horizontal Scaling

```mermaid
graph TB
    subgraph "Load Balancer"
        A[NGINX Load Balancer] --> B[Frontend Instance 1]
        A --> C[Frontend Instance 2]
        A --> D[Frontend Instance N]
    end
    
    subgraph "API Gateway"
        E[FastAPI Gateway] --> F[Backend Instance 1]
        E --> G[Backend Instance 2]
        E --> H[Backend Instance N]
    end
    
    subgraph "Database"
        I[MongoDB Primary] --> J[MongoDB Secondary 1]
        I --> K[MongoDB Secondary 2]
        L[Redis Cluster] --> M[Redis Node 1]
        L --> N[Redis Node 2]
    end
    
    B --> E
    C --> E
    D --> E
    F --> I
    G --> I
    H --> I
    F --> L
    G --> L
    H --> L
```

### Scaling Strategies

#### 1. Application Scaling

- **Stateless Services**: Easy horizontal scaling
- **Load Balancing**: Traffic distribution
- **Auto-scaling**: Dynamic resource allocation
- **Microservices**: Service decomposition

#### 2. Database Scaling

- **Read Replicas**: Query distribution
- **Sharding**: Data partitioning
- **Caching**: Redis for performance
- **Connection Pooling**: Efficient connections

#### 3. Infrastructure Scaling

- **Container Orchestration**: Kubernetes deployment
- **Cloud Services**: AWS/GCP/Azure integration
- **CDN**: Global content delivery
- **Edge Computing**: Local processing
