import { useAuthStore } from "../store/authStore";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const { token, logout } = useAuthStore();
  const navigate = useNavigate();

  if (!token) {
    navigate("/login");
    return null;
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <div className="bg-white shadow-lg p-6 rounded-xl text-center">
        <h1 className="text-2xl font-bold mb-4">Welcome to your Dashboard!</h1>
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
