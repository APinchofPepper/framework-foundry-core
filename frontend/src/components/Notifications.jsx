import { useEffect, useState } from "react";
import { useAuthStore } from "../store/authStore";
import axios from "axios";

export default function Notifications() {
  const { token } = useAuthStore();
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    if (!token) return;
    axios
      .get("http://localhost:8000/notifications/", { headers: { Authorization: `Bearer ${token}` } })
      .then((res) => setNotifications(res.data))
      .catch(console.error);
  }, [token]);

  const markRead = (id) => {
    axios
      .post(`http://localhost:8000/notifications/${id}/read`, {}, { headers: { Authorization: `Bearer ${token}` } })
      .then(() => setNotifications(notifications.filter(n => n.id !== id)))
      .catch(console.error);
  };

  if (!notifications.length) return <p className="text-sm text-gray-500">No new notifications</p>;

  return (
    <div className="bg-gray-100 p-4 rounded mb-4">
      <h2 className="font-semibold mb-2">Notifications</h2>
      <ul>
        {notifications.map((notif) => (
          <li key={notif.id} className="mb-2 p-2 bg-white rounded flex justify-between items-center shadow-sm">
            <div>
              <p className="font-medium">{notif.title}</p>
              <p className="text-sm text-gray-600">{notif.message}</p>
            </div>
            <button
              onClick={() => markRead(notif.id)}
              className="bg-blue-500 text-white px-2 py-1 rounded hover:bg-blue-600"
            >
              Mark Read
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
