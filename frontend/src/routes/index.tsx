import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/')({
  component: HomePage,
});

function HomePage() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Welcome to Food Market Platform
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Browse, compare, and order products from local food markets with ease.
          Designed with accessibility in mind for everyone.
        </p>
        <div className="flex justify-center gap-4">
          <button className="btn btn-primary px-8 py-3 text-lg">
            Browse Markets
          </button>
          <button className="btn btn-outline px-8 py-3 text-lg">
            Learn More
          </button>
        </div>
      </div>

      <div className="grid md:grid-cols-3 gap-8">
        <div className="card">
          <div className="card-header">
            <h3 className="text-xl font-semibold">Easy Shopping</h3>
          </div>
          <div className="card-content">
            <p className="text-gray-600">
              Browse products from multiple markets in one place. Filter by category, 
              price, and availability to find exactly what you need.
            </p>
          </div>
        </div>

        <div className="card">
          <div className="card-header">
            <h3 className="text-xl font-semibold">Accessibility First</h3>
          </div>
          <div className="card-content">
            <p className="text-gray-600">
              Designed with accessibility in mind. Adjustable font sizes, 
              high contrast modes, and keyboard navigation support.
            </p>
          </div>
        </div>

        <div className="card">
          <div className="card-header">
            <h3 className="text-xl font-semibold">Local Markets</h3>
          </div>
          <div className="card-content">
            <p className="text-gray-600">
              Support your local food markets. Fresh, quality products 
              delivered right to your doorstep or ready for pickup.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
} 