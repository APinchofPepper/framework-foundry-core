import { useEffect, useState } from "react";
import { useAuthStore } from "../store/authStore";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const { token, logout } = useAuthStore();
  const [user, setUser] = useState(null);
  const [adminStats, setAdminStats] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate("/login");
      return;
    }

    // fetch user profile
    axios
      .get("http://localhost:8000/users/me", { headers: { Authorization: `Bearer ${token}` } })
      .then((res) => setUser(res.data))
      .catch(() => logout());
  }, [token]);

  // fetch admin stats if user is admin
  useEffect(() => {
    if (user?.role === "admin") {
      axios
        .get("http://localhost:8000/admin/stats", { headers: { Authorization: `Bearer ${token}` } })
        .then((res) => setAdminStats(res.data))
        .catch(console.error);
    }
  }, [user]);

  if (!user) return <p>Loading...</p>;

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto bg-white shadow-lg rounded-xl p-6">
        <h1 className="text-2xl font-bold mb-4">Welcome, {user.full_name || user.email}!</h1>

        {user.role === "admin" && adminStats && (
          <div className="mb-6 p-4 bg-gray-100 rounded">
            <h2 className="text-xl font-semibold mb-2">Admin Stats</h2>
            <ul className="list-disc list-inside">
              <li>Total Users: {adminStats.total_users}</li>
              <li>Active Frameworks: {adminStats.active_frameworks}</li>
              <li>Pending Clients: {adminStats.pending_clients}</li>
            </ul>
          </div>
        )}

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
