export type UserRole = "customer" | "market_admin" | "super_admin";

export interface UserPublic {
  id: string;
  email: string;
  name: string;
  role: UserRole;
  locale: "en" | "ua";
  created_at: string;
  updated_at: string;
}

export interface UserCreate {
  email: string;
  name: string;
  password: string;
  role?: UserRole;
  locale?: "en" | "ua";
}

export interface UserUpdate {
  name?: string;
  locale?: "en" | "ua";
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  user: UserPublic;
} 