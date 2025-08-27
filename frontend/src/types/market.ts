export interface MarketPublic {
  id: string;
  name: string;
  description?: string;
  contact_email: string;
  contact_phone?: string;
  address?: string;
  created_at: string;
  updated_at: string;
}

export interface MarketCreate {
  name: string;
  description?: string;
  contact_email: string;
  contact_phone?: string;
  address?: string;
}

export interface MarketUpdate {
  name?: string;
  description?: string;
  contact_phone?: string;
  address?: string;
} 