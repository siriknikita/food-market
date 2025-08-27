import { createFileRoute, redirect } from '@tanstack/react-router';
import { LoginForm } from '../components/auth/LoginForm';
import { useAuth } from '../contexts/AuthContext';

export const Route = createFileRoute('/login')({
  component: LoginPage,
  beforeLoad: ({ context }) => {
    // Redirect if already logged in
    const auth = context.auth;
    if (auth?.user) {
      throw redirect({
        to: '/',
      });
    }
  },
});

function LoginPage() {
  const { user } = useAuth();

  // Redirect if already logged in
  if (user) {
    return null;
  }

  return (
    <div className="max-w-md mx-auto">
      <div className="card">
        <div className="card-header">
          <h1 className="text-2xl font-bold text-center">Sign In</h1>
          <p className="text-gray-600 text-center">
            Welcome back! Please sign in to your account.
          </p>
        </div>
        <div className="card-content">
          <LoginForm />
        </div>
      </div>
    </div>
  );
} 