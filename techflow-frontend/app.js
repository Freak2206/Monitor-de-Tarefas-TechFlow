import React, { useState } from "react";
import LoginForm from "./components/LoginForm";
import TaskTable from "./components/TaskTable";

function App() {
  const [usuario, setUsuario] = useState(null);

  return (
    <div>
      {!usuario ? (
        <LoginForm onLogin={setUsuario} />
      ) : (
        <TaskTable usuario={usuario} />
      )}
    </div>
  );
}

export default App;
