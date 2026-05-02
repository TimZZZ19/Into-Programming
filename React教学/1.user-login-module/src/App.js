import "./App.css";
import { useState } from "react";

function App() {
  // 1. 创建状态：数字，初始值是 0
  const [count, setCount] = useState(0);
  const [msg, setMsg] = useState("Hello React");
  const [demandList, setDemandList] = useState([
    "交货周期30天",
    "预付50%定金",
    "提供售后服务",
  ]);

  const [inputValue, setInputValue] = useState("");

  function addNewDemand() {
    const newList = [...demandList, "新增服务"];
    setDemandList(newList);
  }

  const deleteItem = (index) => {
    const newList = demandList.filter((_, i) => i != index);
    setDemandList(newList);
  };

  const inputHandler = (event) => {
    setInputValue(event.target.value);
  };

  // 用户数组：员工资料库
  // const validUsers = [
  //   { id: 1, name: "张三", company: "A公司" },
  //   { id: 2, name: "李四", company: "B公司" },
  //   { id: 3, name: "王五", company: "C公司" }
  // ];

  // // map()
  // // filter()
  // // find()

  return (
    // <div>
    //   <p>数字：{count}</p>
    //   {/* 点击按钮 → 修改状态 */}
    //   <button onClick={() => setCount(count + 1)}>点我+1</button>

    //   <p>Display Message: {msg}</p>
    //   <button onClick={() => setMsg("abc")}>点我改文字</button>
    // </div>
    // <div>
    //   <h3>Demand List</h3>
    //   <ul>
    //     {/* <li>{demandList[0]}</li>
    //     <li>{demandList[1]}</li>
    //     <li>{demandList[2]}</li> */}

    //     {demandList.map((item, index) => (
    //       <li key={index}>
    //         {item}
    //         <button onClick={() => deleteItem(index)}>delete</button>
    //       </li>
    //     ))}
    //   </ul>
    //   {/* click handler */}
    //   <button onClick={() => addNewDemand()}>添加新的需求</button>
    // </div>
    <div>
      <input value={inputValue} onChange={(event) => inputHandler(event)} />
    </div>
  );
}

export default App;
