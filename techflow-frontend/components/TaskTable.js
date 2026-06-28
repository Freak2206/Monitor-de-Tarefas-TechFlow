import React, { useEffect, useState } from "react";

function TaskTable({ usuario }) {
  const [tarefas, setTarefas] = useState([]);
  const [titulo, setTitulo] = useState("");
  const [descricao, setDescricao] = useState("");
  const [prioridade, setPrioridade] = useState("");
  const [status, setStatus] = useState("");

  const listar = async () => {
    const res = await fetch("http://localhost:5000/tasks");
    const data = await res.json();
    setTarefas(data);
  };

  const adicionar = async () => {
    const res = await fetch("http://localhost:5000/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ titulo, descricao, prioridade, status })
    });
    await res.json();
    listar();
  };

  const remover = async (titulo) => {
    await fetch(`http://localhost:5000/tasks/${titulo}`, { method: "DELETE" });
    listar();
  };

  useEffect(() => {
    listar();
  }, []);

  return (
    <div>
      <input placeholder="Título" value={titulo} onChange={e => setTitulo(e.target.value)} />
      <input placeholder="Descrição" value={descricao} onChange={e => setDescricao(e.target.value)} />
      <input placeholder="Prioridade" value={prioridade} onChange={e => setPrioridade(e.target.value)} />
      <input placeholder="Status" value={status} onChange={e => setStatus(e.target.value)} />
      <button onClick={adicionar}>Adicionar</button>

      <table border="1">
        <thead>
          <tr>
            <th>Título</th>
            <th>Descrição</th>
            <th>Prioridade</th>
            <th>Status</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {tarefas.map((t, i) => (
            <tr key={i}>
              <td>{t.titulo}</td>
              <td>{t.descricao}</td>
              <td>{t.prioridade}</td>
              <td>{t.status}</td>
              <td><button onClick={() => remover(t.titulo)}>Remover</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TaskTable;
