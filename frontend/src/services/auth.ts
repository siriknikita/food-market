import { apiService } from './api';
import type { UserCreate, UserPublic, LoginRequest, LoginResponse, UserUpdate } from '../types/user';

export const authService = {
  async register(userData: UserCreate): Promise<UserPublic> {
    return apiService.post<UserPublic>('/auth/register', userData);
  },

  async login(credentials: LoginRequest): Promise<LoginResponse> {
    const formData = new FormData();
    formData.append('username', credentials.email);
    formData.append('password', credentials.password);

    const response = await fetch(`${apiService['baseURL']}/auth/login`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
    }

    return response.json();
  },

  async getCurrentUser(): Promise<UserPublic> {
    return apiService.get<UserPublic>('/auth/me');
  },

  async updateUser(userData: UserUpdate): Promise<UserPublic> {
    return apiService.put<UserPublic>('/auth/me', userData);
  },
}; 