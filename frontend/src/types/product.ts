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
  created_at: string;
  updated_at: string;
}

export interface ProductCreate {
  market_id: string;
  name: string;
  description?: string;
  price: number;
  stock_quantity: number;
  category: string;
  sub_category?: string;
  tags?: string[];
  images?: string[];
}

export interface ProductUpdate {
  name?: string;
  description?: string;
  price?: number;
  stock_quantity?: number;
  category?: string;
  sub_category?: string;
  tags?: string[];
  images?: string[];
}

export interface ProductFilters {
  category?: string;
  sub_category?: string;
  tags?: string[];
  min_price?: number;
  max_price?: number;
  in_stock?: boolean;
  search?: string;
} 