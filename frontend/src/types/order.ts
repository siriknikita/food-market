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
  created_at: string;
  updated_at: string;
}

export interface OrderCreate {
  user_id: string;
  market_id: string;
  items: OrderItem[];
  comment?: string;
}

export interface OrderUpdate {
  status?: OrderStatus;
  comment?: string;
} 