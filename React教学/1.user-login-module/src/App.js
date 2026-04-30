import "./App.css";
import { useState } from "react";

function App() {
  // 1. 创建状态：数字，初始值是 0
  const [count, setCount] = useState(0);

  console.log("I'm running");

  return (
    <div>
      <p>数字：{count}</p>
      {/* 点击按钮 → 修改状态 */}
      <button onClick={() => setCount(count + 1)}>点我+1</button>
    </div>
  );
}

export default App;
