import { useEffect, useState } from "react";
import { fetchLeaderboard } from "./api";

export default function Leaderboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchLeaderboard().then(setData);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>🏆 Top Users (Last 24h)</h2>

      {data.length === 0 && <p>No activity yet</p>}

      <ul>
        {data.map((user, idx) => (
          <li key={idx}>
            <strong>{user.user__username}</strong> — {user.karma} karma
          </li>
        ))}
      </ul>
    </div>
  );
}
