# Food Market Platform

A web-based food market platform with accessibility-first design, supporting elderly and mobility-limited individuals. The platform allows food markets to register, manage products, and enables customers to browse and order products.

## Features

### Customer-facing

- Browse product assortments from multiple markets
- Filter and search by category, tags, and stock availability
- Place orders with custom comments
- View and manage order history
- Customize font size, theme, and language preferences
- Accessibility-first design with high contrast and keyboard navigation

### Admin-facing

- Market management interface
- Product catalog management
- Order processing and status updates
- Statistics and analytics dashboard
- Role-based authentication system

## Technology Stack

### Frontend

- **React 18** with TypeScript
- **TanStack Router** for routing
- **TanStack Query** for data fetching
- **Tailwind CSS** for styling
- **React Hook Form** with Zod validation
- **i18next** for internationalization (English/Ukrainian)

### Backend

- **FastAPI** (Python) with async support
- **MongoDB** with Motor async driver
- **JWT** authentication
- **Pydantic** for data validation
- **Pytest** for testing (TDD approach)

### Infrastructure

- **Docker** and **Docker Compose** for containerization
- **Nginx** for frontend serving
- **MongoDB** for data persistence

## Project Structure

```
food-market/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/v1/         # API routes
│   │   ├── auth/           # Authentication
│   │   ├── models/         # Pydantic models
│   │   ├── config.py       # Configuration
│   │   ├── database.py     # Database connection
│   │   └── main.py         # FastAPI app
│   ├── tests/              # Backend tests
│   ├── Dockerfile          # Backend container
│   └── pyproject.toml      # Python dependencies
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── contexts/       # React contexts
│   │   ├── routes/         # TanStack Router routes
│   │   ├── services/       # API services
│   │   ├── types/          # TypeScript types
│   │   └── App.tsx         # Main app component
│   ├── Dockerfile          # Frontend container
│   └── package.json        # Node.js dependencies
├── docs/                   # Documentation
├── docker-compose.yml      # Docker Compose configuration
└── README.md              # This file
```

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Using Docker (Recommended)

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd food-market
   ```

2. **Start the application**

   ```bash
   # Production build
   docker-compose up -d
   
   # Development mode with hot reloading
   docker-compose --profile dev up -d
   ```

3. **Access the application**
   - Frontend: <http://localhost> (production) or <http://localhost:5173> (development)
   - Backend API: <http://localhost:8000>
   - API Documentation: <http://localhost:8000/docs>

### Local Development

#### Backend Setup

```bash
cd backend
uv install
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

### Authentication

- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user
- `PUT /api/v1/auth/me` - Update current user

### Markets (Planned)

- `GET /api/v1/markets` - List markets
- `POST /api/v1/markets` - Create market
- `GET /api/v1/markets/{id}` - Get market details
- `PUT /api/v1/markets/{id}` - Update market

### Products (Planned)

- `GET /api/v1/products` - List products with filters
- `POST /api/v1/products` - Create product
- `GET /api/v1/products/{id}` - Get product details
- `PUT /api/v1/products/{id}` - Update product

### Orders (Planned)

- `GET /api/v1/orders` - List orders
- `POST /api/v1/orders` - Create order
- `GET /api/v1/orders/{id}` - Get order details
- `PUT /api/v1/orders/{id}` - Update order status

## Testing

### Backend Tests

```bash
cd backend
uv run pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Accessibility Features

- **Font Size Control**: Small, Medium, Large options
- **Theme Toggle**: Light and Dark modes
- **High Contrast Mode**: Enhanced visibility
- **Language Support**: English and Ukrainian
- **Keyboard Navigation**: Full keyboard accessibility
- **Screen Reader Support**: ARIA labels and semantic HTML

## Development Guidelines

### Code Style

- **Backend**: Follow PEP 8 with Black formatting
- **Frontend**: ESLint and Prettier configuration
- **TypeScript**: Strict mode enabled
- **Testing**: TDD approach with comprehensive coverage

### Git Workflow

1. Create feature branch from `main`
2. Write tests first (TDD)
3. Implement functionality
4. Ensure all tests pass
5. Create pull request

### Environment Variables

#### Backend (.env)

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=food_market
SECRET_KEY=your-secret-key
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

#### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000/api/v1
```

## Deployment

### Production Deployment

1. Set up production environment variables
2. Build and push Docker images
3. Deploy using Docker Compose or Kubernetes
4. Configure reverse proxy (Nginx)
5. Set up SSL certificates
6. Configure monitoring and logging

### Environment-Specific Configurations

- **Development**: Hot reloading, debug mode
- **Staging**: Production-like environment for testing
- **Production**: Optimized builds, security hardening

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow the TDD approach
4. Ensure accessibility compliance
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:

- Create an issue in the repository
- Check the [documentation](docs/)
- Review the [API documentation](http://localhost:8000/docs)

## Roadmap

### Phase 1: Core Features ✅

- [x] Project setup and architecture
- [x] Authentication system
- [x] Basic frontend structure
- [x] Docker containerization

### Phase 2: Market & Product Management

- [ ] Market registration and management
- [ ] Product catalog with CRUD operations
- [ ] Image upload and management
- [ ] Search and filtering

### Phase 3: Order System

- [ ] Shopping cart functionality
- [ ] Order placement and management
- [ ] Order status tracking
- [ ] Payment integration

### Phase 4: Advanced Features

- [ ] Real-time notifications
- [ ] Advanced analytics
- [ ] Mobile app
- [ ] Multi-language support expansion
