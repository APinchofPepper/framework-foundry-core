import { create } from "zustand";
import axios from "axios";

const API_URL = "http://localhost:8000/auth";

export const useAuthStore = create((set) => ({
  user: null,
  token: localStorage.getItem("token") || null,
  loading: false,
  error: null,

  register: async (email, password, fullName) => {
    set({ loading: true, error: null });
    try {
      await axios.post(`${API_URL}/register`, { email, password, full_name: fullName });
      set({ loading: false });
      return true;
    } catch (err) {
      set({ loading: false, error: err.response?.data?.detail || "Registration failed" });
      return false;
    }
  },

  login: async (email, password) => {
    set({ loading: true, error: null });
    try {
      const { data } = await axios.post(`${API_URL}/login`, { email, password });
      localStorage.setItem("token", data.access_token);
      set({ token: data.access_token, loading: false });
      return true;
    } catch (err) {
      set({ loading: false, error: err.response?.data?.detail || "Login failed" });
      return false;
    }
  },

  logout: () => {
    localStorage.removeItem("token");
    set({ user: null, token: null });
  },
}));
