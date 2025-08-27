import { Link } from '@tanstack/react-router';
import { useAuth } from '../../contexts/AuthContext';
import { AccessibilityControls } from './AccessibilityControls';

export function Header() {
  const { user, logout } = useAuth();

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-lg">F</span>
            </div>
            <span className="text-xl font-bold text-gray-900">Food Market</span>
          </Link>

          {/* Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            <Link
              to="/"
              className="text-gray-600 hover:text-gray-900 transition-colors"
              activeProps={{ className: "text-primary-600 font-medium" }}
            >
              Home
            </Link>
            <Link
              to="/markets"
              className="text-gray-600 hover:text-gray-900 transition-colors"
              activeProps={{ className: "text-primary-600 font-medium" }}
            >
              Markets
            </Link>
            <Link
              to="/products"
              className="text-gray-600 hover:text-gray-900 transition-colors"
              activeProps={{ className: "text-primary-600 font-medium" }}
            >
              Products
            </Link>
            {user && (
              <Link
                to="/orders"
                className="text-gray-600 hover:text-gray-900 transition-colors"
                activeProps={{ className: "text-primary-600 font-medium" }}
              >
                My Orders
              </Link>
            )}
          </nav>

          {/* Right side */}
          <div className="flex items-center space-x-4">
            <AccessibilityControls />
            
            {user ? (
              <div className="flex items-center space-x-4">
                <span className="text-sm text-gray-600">
                  Welcome, {user.name}
                </span>
                <button
                  onClick={logout}
                  className="btn btn-outline"
                >
                  Logout
                </button>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <Link
                  to="/login"
                  className="btn btn-outline"
                >
                  Sign In
                </Link>
                <Link
                  to="/register"
                  className="btn btn-primary"
                >
                  Sign Up
                </Link>
              </div>
            )}
          </div>
        </div>
      </div>
    </header>
  );
} 