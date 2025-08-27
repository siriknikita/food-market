# Frontend Development Guide

## 🎯 Overview

The Food Market Platform frontend is built with **React**, **TypeScript**, and **TailwindCSS**, prioritizing accessibility and user experience for elderly and mobility-limited users.

### Tech Stack

- **React 18** - UI library with hooks and concurrent features
- **TypeScript** - Type safety and developer experience
- **TanStack Router** - Type-safe routing
- **React Query** - Server state management
- **ShadCN UI** - Accessible component library
- **TailwindCSS** - Utility-first CSS framework
- **i18next** - Internationalization
- **Vite** - Fast build tool and dev server

---

## 🏗️ Project Structure

```text
frontend/
├── public/
│   ├── images/
│   ├── locales/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ui/              # ShadCN UI components
│   │   ├── common/          # Reusable components
│   │   ├── layout/          # Layout components
│   │   ├── forms/           # Form components
│   │   ├── product/         # Product-related components
│   │   ├── order/           # Order-related components
│   │   └── admin/           # Admin components
│   ├── hooks/
│   │   ├── useAuth.ts       # Authentication hook
│   │   ├── useCart.ts       # Shopping cart hook
│   │   ├── useOrders.ts     # Orders management hook
│   │   ├── useMarkets.ts    # Markets data hook
│   │   └── useProducts.ts   # Products data hook
│   ├── pages/
│   │   ├── Home.tsx         # Landing page
│   │   ├── Markets.tsx      # Markets listing
│   │   ├── Products.tsx     # Products catalog
│   │   ├── ProductDetail.tsx # Product details
│   │   ├── Cart.tsx         # Shopping cart
│   │   ├── Checkout.tsx     # Order checkout
│   │   ├── Orders.tsx       # Order history
│   │   └── Admin/           # Admin pages
│   ├── services/
│   │   ├── api.ts           # API client
│   │   ├── auth.ts          # Authentication service
│   │   └── storage.ts       # Local storage utilities
│   ├── stores/
│   │   ├── authStore.ts     # Authentication state
│   │   ├── cartStore.ts     # Shopping cart state
│   │   └── uiStore.ts       # UI state (theme, locale)
│   ├── types/
│   │   ├── user.ts          # User types
│   │   ├── market.ts        # Market types
│   │   ├── product.ts       # Product types
│   │   ├── order.ts         # Order types
│   │   └── api.ts           # API response types
│   ├── utils/
│   │   ├── constants.ts     # Application constants
│   │   ├── helpers.ts       # Utility functions
│   │   ├── validators.ts    # Form validation
│   │   └── accessibility.ts # Accessibility utilities
│   ├── styles/
│   │   ├── globals.css      # Global styles
│   │   └── components.css   # Component styles
│   ├── App.tsx              # Main app component
│   ├── main.tsx             # App entry point
│   └── vite-env.d.ts        # Vite type definitions
├── package.json
├── tsconfig.json
├── tailwind.config.js
├── vite.config.ts
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** 18+ and **npm** or **bun**
- **Git** for version control
- **VS Code** with recommended extensions

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/food-market.git
cd food-market/frontend

# Install dependencies
npm install
# or
bun install

# Start development server
npm run dev
# or
bun dev
```

### Development Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run tests
npm run test

# Run tests in watch mode
npm run test:watch

# Run linting
npm run lint

# Run type checking
npm run type-check

# Format code
npm run format
```

---

## 🎨 Component Development

### Component Structure

All components follow a consistent structure:

```typescript
// components/common/Button.tsx
import React from 'react';
import { cn } from '@/utils/helpers';
import { ButtonProps } from './Button.types';

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'medium',
  disabled = false,
  className,
  ...props
}) => {
  return (
    <button
      className={cn(
        'button',
        `button--${variant}`,
        `button--${size}`,
        disabled && 'button--disabled',
        className
      )}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
};
```

### Component Types

```typescript
// components/common/Button.types.ts
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'small' | 'medium' | 'large';
  loading?: boolean;
}
```

### Accessibility Guidelines

#### 1. Semantic HTML

```typescript
// ✅ Good - Semantic button
<button type="button" onClick={handleClick}>
  Submit Order
</button>

// ❌ Bad - Non-semantic div
<div onClick={handleClick}>
  Submit Order
</div>
```

#### 2. ARIA Labels

```typescript
// ✅ Good - Proper ARIA labels
<button
  aria-label="Add apples to cart"
  aria-describedby="apple-description"
  onClick={addToCart}
>
  Add to Cart
</button>
<div id="apple-description">
  Fresh organic apples, $2.99 per kg
</div>
```

#### 3. Keyboard Navigation

```typescript
// ✅ Good - Keyboard accessible
const handleKeyDown = (event: React.KeyboardEvent) => {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    handleClick();
  }
};

<button
  onClick={handleClick}
  onKeyDown={handleKeyDown}
  tabIndex={0}
>
  Click me
</button>
```

#### 4. Focus Management

```typescript
// ✅ Good - Focus management
const modalRef = useRef<HTMLDivElement>(null);

useEffect(() => {
  if (isOpen && modalRef.current) {
    modalRef.current.focus();
  }
}, [isOpen]);

<div
  ref={modalRef}
  tabIndex={-1}
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
>
  <h2 id="modal-title">Order Confirmation</h2>
  {/* Modal content */}
</div>
```

---

## 🎯 Accessibility-First Development

### Font Size Management

```typescript
// hooks/useFontSize.ts
import { useState, useEffect } from 'react';

export type FontSize = 'small' | 'medium' | 'large' | 'extra-large';

export const useFontSize = () => {
  const [fontSize, setFontSize] = useState<FontSize>(() => {
    const saved = localStorage.getItem('fontSize');
    return (saved as FontSize) || 'medium';
  });

  useEffect(() => {
    document.documentElement.setAttribute('data-font-size', fontSize);
    localStorage.setItem('fontSize', fontSize);
  }, [fontSize]);

  return { fontSize, setFontSize };
};
```

### Theme Management

```typescript
// hooks/useTheme.ts
import { useState, useEffect } from 'react';

export type Theme = 'light' | 'dark' | 'high-contrast';

export const useTheme = () => {
  const [theme, setTheme] = useState<Theme>(() => {
    const saved = localStorage.getItem('theme');
    return (saved as Theme) || 'light';
  });

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  return { theme, setTheme };
};
```

### Accessibility Components

```typescript
// components/common/AccessibilityControls.tsx
import React from 'react';
import { useFontSize } from '@/hooks/useFontSize';
import { useTheme } from '@/hooks/useTheme';
import { Button } from './Button';

export const AccessibilityControls: React.FC = () => {
  const { fontSize, setFontSize } = useFontSize();
  const { theme, setTheme } = useTheme();

  return (
    <div className="accessibility-controls" role="toolbar" aria-label="Accessibility controls">
      <div className="font-size-controls">
        <label htmlFor="font-size">Font Size:</label>
        <select
          id="font-size"
          value={fontSize}
          onChange={(e) => setFontSize(e.target.value as FontSize)}
        >
          <option value="small">Small</option>
          <option value="medium">Medium</option>
          <option value="large">Large</option>
          <option value="extra-large">Extra Large</option>
        </select>
      </div>
      
      <div className="theme-controls">
        <label htmlFor="theme">Theme:</label>
        <select
          id="theme"
          value={theme}
          onChange={(e) => setTheme(e.target.value as Theme)}
        >
          <option value="light">Light</option>
          <option value="dark">Dark</option>
          <option value="high-contrast">High Contrast</option>
        </select>
      </div>
    </div>
  );
};
```

---

## 🌍 Internationalization

### i18next Setup

```typescript
// i18n/index.ts
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import enTranslations from './locales/en.json';
import uaTranslations from './locales/ua.json';

i18n
  .use(initReactI18next)
  .init({
    resources: {
      en: { translation: enTranslations },
      ua: { translation: uaTranslations }
    },
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
```

### Translation Files

```json
// locales/en.json
{
  "common": {
    "loading": "Loading...",
    "error": "An error occurred",
    "save": "Save",
    "cancel": "Cancel",
    "delete": "Delete",
    "edit": "Edit",
    "add": "Add"
  },
  "navigation": {
    "home": "Home",
    "markets": "Markets",
    "products": "Products",
    "cart": "Cart",
    "orders": "Orders",
    "account": "Account"
  },
  "products": {
    "addToCart": "Add to Cart",
    "outOfStock": "Out of Stock",
    "price": "Price",
    "quantity": "Quantity",
    "description": "Description",
    "category": "Category"
  }
}
```

```json
// locales/ua.json
{
  "common": {
    "loading": "Завантаження...",
    "error": "Сталася помилка",
    "save": "Зберегти",
    "cancel": "Скасувати",
    "delete": "Видалити",
    "edit": "Редагувати",
    "add": "Додати"
  },
  "navigation": {
    "home": "Головна",
    "markets": "Ринки",
    "products": "Товари",
    "cart": "Кошик",
    "orders": "Замовлення",
    "account": "Акаунт"
  },
  "products": {
    "addToCart": "Додати в кошик",
    "outOfStock": "Немає в наявності",
    "price": "Ціна",
    "quantity": "Кількість",
    "description": "Опис",
    "category": "Категорія"
  }
}
```

### Using Translations

```typescript
// components/common/Button.tsx
import { useTranslation } from 'react-i18next';

export const Button: React.FC<ButtonProps> = ({ children, ...props }) => {
  const { t } = useTranslation();
  
  return (
    <button {...props}>
      {typeof children === 'string' ? t(children) : children}
    </button>
  );
};

// Usage
<Button>{t('common.save')}</Button>
```

---

## 🔄 State Management

### React Query for Server State

```typescript
// hooks/useMarkets.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/services/api';
import { Market, MarketCreate } from '@/types/market';

export const useMarkets = () => {
  return useQuery({
    queryKey: ['markets'],
    queryFn: () => api.markets.list(),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
};

export const useMarket = (id: string) => {
  return useQuery({
    queryKey: ['markets', id],
    queryFn: () => api.markets.get(id),
    enabled: !!id,
  });
};

export const useCreateMarket = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: (data: MarketCreate) => api.markets.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['markets'] });
    },
  });
};
```

### Context for Client State

```typescript
// stores/cartStore.ts
import React, { createContext, useContext, useReducer } from 'react';
import { CartItem, CartState, CartAction } from '@/types/cart';

const CartContext = createContext<{
  state: CartState;
  dispatch: React.Dispatch<CartAction>;
} | null>(null);

const cartReducer = (state: CartState, action: CartAction): CartState => {
  switch (action.type) {
    case 'ADD_ITEM':
      const existingItem = state.items.find(
        item => item.product_id === action.payload.product_id
      );
      
      if (existingItem) {
        return {
          ...state,
          items: state.items.map(item =>
            item.product_id === action.payload.product_id
              ? { ...item, quantity: item.quantity + action.payload.quantity }
              : item
          )
        };
      }
      
      return {
        ...state,
        items: [...state.items, action.payload]
      };
      
    case 'REMOVE_ITEM':
      return {
        ...state,
        items: state.items.filter(item => item.product_id !== action.payload)
      };
      
    case 'UPDATE_QUANTITY':
      return {
        ...state,
        items: state.items.map(item =>
          item.product_id === action.payload.product_id
            ? { ...item, quantity: action.payload.quantity }
            : item
        )
      };
      
    case 'CLEAR_CART':
      return {
        ...state,
        items: []
      };
      
    default:
      return state;
  }
};

export const CartProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(cartReducer, { items: [] });
  
  return (
    <CartContext.Provider value={{ state, dispatch }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
};
```

---

## 🎨 Styling with TailwindCSS

### Custom Configuration

```javascript
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          500: '#0ea5e9',
          600: '#0284c7',
          700: '#0369a1',
          900: '#0c4a6e',
        },
        secondary: {
          50: '#f8fafc',
          100: '#f1f5f9',
          500: '#64748b',
          600: '#475569',
          700: '#334155',
          900: '#0f172a',
        }
      },
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1rem' }],
        'sm': ['0.875rem', { lineHeight: '1.25rem' }],
        'base': ['1rem', { lineHeight: '1.5rem' }],
        'lg': ['1.125rem', { lineHeight: '1.75rem' }],
        'xl': ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

### Accessibility-First Classes

```typescript
// utils/accessibility.ts
export const accessibilityClasses = {
  // Focus styles
  focusRing: 'focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2',
  
  // High contrast
  highContrast: 'text-gray-900 bg-white border-2 border-gray-900',
  
  // Large touch targets
  largeTouchTarget: 'min-h-[44px] min-w-[44px]',
  
  // Readable text
  readableText: 'text-base leading-relaxed',
  
  // Large text
  largeText: 'text-lg leading-relaxed',
  
  // Extra large text
  extraLargeText: 'text-xl leading-relaxed',
} as const;
```

### Component Styling

```typescript
// components/common/Button.tsx
import { accessibilityClasses } from '@/utils/accessibility';

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'medium',
  disabled = false,
  className,
  ...props
}) => {
  const baseClasses = [
    'inline-flex items-center justify-center rounded-md font-medium transition-colors',
    accessibilityClasses.focusRing,
    accessibilityClasses.largeTouchTarget,
    'disabled:opacity-50 disabled:pointer-events-none'
  ];
  
  const variantClasses = {
    primary: 'bg-primary-600 text-white hover:bg-primary-700',
    secondary: 'bg-secondary-100 text-secondary-900 hover:bg-secondary-200',
    outline: 'border border-secondary-300 bg-transparent hover:bg-secondary-50',
    ghost: 'hover:bg-secondary-100'
  };
  
  const sizeClasses = {
    small: 'h-8 px-3 text-sm',
    medium: 'h-10 px-4 text-base',
    large: 'h-12 px-6 text-lg'
  };
  
  return (
    <button
      className={cn(
        baseClasses,
        variantClasses[variant],
        sizeClasses[size],
        className
      )}
      disabled={disabled}
      {...props}
    />
  );
};
```

---

## 🧪 Testing

### Component Testing

```typescript
// components/common/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: 'Click me' })).toBeInTheDocument();
  });
  
  it('handles click events', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click me</Button>);
    
    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });
  
  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });
  
  it('has proper accessibility attributes', () => {
    render(<Button aria-label="Submit form">Submit</Button>);
    expect(screen.getByRole('button')).toHaveAttribute('aria-label', 'Submit form');
  });
});
```

### Hook Testing

```typescript
// hooks/useCart.test.ts
import { renderHook, act } from '@testing-library/react';
import { CartProvider, useCart } from '@/stores/cartStore';

const wrapper = ({ children }: { children: React.ReactNode }) => (
  <CartProvider>{children}</CartProvider>
);

describe('useCart', () => {
  it('adds item to cart', () => {
    const { result } = renderHook(() => useCart(), { wrapper });
    
    act(() => {
      result.current.dispatch({
        type: 'ADD_ITEM',
        payload: { product_id: '1', quantity: 2, price: 10 }
      });
    });
    
    expect(result.current.state.items).toHaveLength(1);
    expect(result.current.state.items[0].quantity).toBe(2);
  });
  
  it('updates item quantity', () => {
    const { result } = renderHook(() => useCart(), { wrapper });
    
    // Add item first
    act(() => {
      result.current.dispatch({
        type: 'ADD_ITEM',
        payload: { product_id: '1', quantity: 1, price: 10 }
      });
    });
    
    // Update quantity
    act(() => {
      result.current.dispatch({
        type: 'UPDATE_QUANTITY',
        payload: { product_id: '1', quantity: 3 }
      });
    });
    
    expect(result.current.state.items[0].quantity).toBe(3);
  });
});
```

### Integration Testing

```typescript
// pages/Products.test.tsx
import { render, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Products } from './Products';
import { api } from '@/services/api';

// Mock API
jest.mock('@/services/api');

const queryClient = new QueryClient({
  defaultOptions: {
    queries: { retry: false },
    mutations: { retry: false },
  },
});

const wrapper = ({ children }: { children: React.ReactNode }) => (
  <QueryClientProvider client={queryClient}>
    {children}
  </QueryClientProvider>
);

describe('Products Page', () => {
  it('displays products after loading', async () => {
    const mockProducts = [
      { id: '1', name: 'Apples', price: 2.99, stock_quantity: 10 },
      { id: '2', name: 'Bananas', price: 1.99, stock_quantity: 15 }
    ];
    
    (api.products.list as jest.Mock).mockResolvedValue(mockProducts);
    
    render(<Products />, { wrapper });
    
    // Show loading state
    expect(screen.getByText('Loading...')).toBeInTheDocument();
    
    // Wait for products to load
    await waitFor(() => {
      expect(screen.getByText('Apples')).toBeInTheDocument();
      expect(screen.getByText('Bananas')).toBeInTheDocument();
    });
  });
});
```

---

## 🚀 Performance Optimization

### Code Splitting

```typescript
// App.tsx
import { lazy, Suspense } from 'react';
import { LoadingSpinner } from '@/components/common/LoadingSpinner';

// Lazy load pages
const Home = lazy(() => import('@/pages/Home'));
const Markets = lazy(() => import('@/pages/Markets'));
const Products = lazy(() => import('@/pages/Products'));
const Cart = lazy(() => import('@/pages/Cart'));
const Orders = lazy(() => import('@/pages/Orders'));

export const App = () => {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/markets" element={<Markets />} />
          <Route path="/products" element={<Products />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/orders" element={<Orders />} />
        </Routes>
      </Router>
    </Suspense>
  );
};
```

### Image Optimization

```typescript
// components/common/OptimizedImage.tsx
import React, { useState } from 'react';

interface OptimizedImageProps {
  src: string;
  alt: string;
  className?: string;
  fallback?: string;
}

export const OptimizedImage: React.FC<OptimizedImageProps> = ({
  src,
  alt,
  className,
  fallback = '/images/placeholder.jpg'
}) => {
  const [imageSrc, setImageSrc] = useState(src);
  const [isLoading, setIsLoading] = useState(true);
  const [hasError, setHasError] = useState(false);

  const handleLoad = () => {
    setIsLoading(false);
  };

  const handleError = () => {
    setHasError(true);
    setImageSrc(fallback);
    setIsLoading(false);
  };

  return (
    <div className={`relative ${className}`}>
      {isLoading && (
        <div className="absolute inset-0 bg-gray-200 animate-pulse" />
      )}
      <img
        src={imageSrc}
        alt={alt}
        className={`w-full h-full object-cover ${
          isLoading ? 'opacity-0' : 'opacity-100'
        }`}
        onLoad={handleLoad}
        onError={handleError}
        loading="lazy"
      />
    </div>
  );
};
```

### Memoization

```typescript
// components/product/ProductList.tsx
import React, { useMemo } from 'react';
import { Product } from '@/types/product';

interface ProductListProps {
  products: Product[];
  filter: string;
  sortBy: 'name' | 'price' | 'category';
}

export const ProductList: React.FC<ProductListProps> = React.memo(({
  products,
  filter,
  sortBy
}) => {
  const filteredAndSortedProducts = useMemo(() => {
    let result = products;
    
    // Filter
    if (filter) {
      result = result.filter(product =>
        product.name.toLowerCase().includes(filter.toLowerCase()) ||
        product.description?.toLowerCase().includes(filter.toLowerCase())
      );
    }
    
    // Sort
    result = [...result].sort((a, b) => {
      switch (sortBy) {
        case 'name':
          return a.name.localeCompare(b.name);
        case 'price':
          return a.price - b.price;
        case 'category':
          return a.category.localeCompare(b.category);
        default:
          return 0;
      }
    });
    
    return result;
  }, [products, filter, sortBy]);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {filteredAndSortedProducts.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
});
```

---

## 🔧 Development Tools

### VS Code Extensions

```json
// .vscode/extensions.json
{
  "recommendations": [
    "bradlc.vscode-tailwindcss",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-typescript-next",
    "formulahendry.auto-rename-tag",
    "christian-kohler.path-intellisense",
    "ms-vscode.vscode-eslint",
    "ms-vscode.vscode-json"
  ]
}
```

### Prettier Configuration

```json
// .prettierrc
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false
}
```

### ESLint Configuration

```javascript
// .eslintrc.js
module.exports = {
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'plugin:jsx-a11y/recommended'
  ],
  plugins: ['@typescript-eslint', 'react', 'jsx-a11y'],
  rules: {
    'react/react-in-jsx-scope': 'off',
    'react/prop-types': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }]
  },
  settings: {
    react: {
      version: 'detect'
    }
  }
};
```

---

## 📱 Mobile-First Development

### Responsive Design

```typescript
// components/layout/Header.tsx
export const Header: React.FC = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <header className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <div className="flex-shrink-0">
            <img className="h-8 w-auto" src="/logo.svg" alt="Food Market" />
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex space-x-8">
            <NavLink to="/">Home</NavLink>
            <NavLink to="/markets">Markets</NavLink>
            <NavLink to="/products">Products</NavLink>
            <NavLink to="/cart">Cart</NavLink>
          </nav>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="text-gray-500 hover:text-gray-700"
              aria-label="Toggle mobile menu"
            >
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMobileMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
              <MobileNavLink to="/">Home</MobileNavLink>
              <MobileNavLink to="/markets">Markets</MobileNavLink>
              <MobileNavLink to="/products">Products</MobileNavLink>
              <MobileNavLink to="/cart">Cart</MobileNavLink>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};
```

### Touch-Friendly Components

```typescript
// components/common/TouchButton.tsx
export const TouchButton: React.FC<ButtonProps> = ({ children, ...props }) => {
  return (
    <button
      className="min-h-[44px] min-w-[44px] px-4 py-2 text-base font-medium rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 active:scale-95"
      {...props}
    >
      {children}
    </button>
  );
};
```
