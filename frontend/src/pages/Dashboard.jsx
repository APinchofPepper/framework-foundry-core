import { useEffect, useState } from "react";
import { useAuthStore } from "../store/authStore";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const { token, logout } = useAuthStore();
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate("/login");
      return;
    }
    axios
      .get("http://localhost:8000/users/me", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => setUser(res.data))
      .catch(() => logout());
  }, [token]);

  if (!user) return <p>Loading...</p>;

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <div className="bg-white shadow-lg p-6 rounded-xl text-center">
        <h1 className="text-2xl font-bold mb-4">Welcome, {user.full_name || user.email}!</h1>
        <p className="mb-6">You are logged in 🎉</p>
        <button
          onClick={logout}
          className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
