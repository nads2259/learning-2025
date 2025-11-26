import React, {useState,useEffect} from 'react';
import './App.css';

const API_URL = 'http://localhost:5000/api/tasks';

function App()
{

  const [task,setTask] = useState("");
  const [taskList,setTaskList] = useState([]);
  const [loading,setLoading] = useState(false);

  useEffect(() => {
    fetchTasks();
  },[]);

  async function fetchTasks()
  {
    try 
    {
      setLoading(true);
      const response = await fetch(API_URL);
      const data = await response.json();
      setTaskList(data);
    }
    catch (err)
    {
      console.error('Error loading tasks: ',err);
    }
    finally 
    {
      setLoading(false);
    }
  }




  async function addTask(event)
  {
    event.preventDefault();

    const trimmed = task.trim();
    if (!trimmed) return;

    const response = await fetch(
      API_URL,
      {
        method : 'POST',
        headers : {'Content-Type' : 'application/json'},
        body : JSON.stringify({text : trimmed}),
      }
    );  

    const newTask = await response.json();
    setTaskList((prev) => [newTask,...prev]);
    setTask("");
  }

  async function deleteTask(taskID)
  {
    try 
    {
      const response = await fetch(`${API_URL}/${taskID}`,
        {
          method : 'DELETE',
        })

      if (!response.ok)
      {
        console.error('Failed to delete task')
        return;
      }

      const result = await response.json();

      if (result.deleted)
      {
        setTaskList((prev) => prev.filter((task) => task.id != taskID));
      }
    }
    catch (err)
    {
      console.error('Error deleting task : ',err);
    }
  }

  return (

    <div className = 'app'>

      <header className = 'app-header'>
        <h1 className = 'app-title'> To-Do App </h1>
      </header>

      <main className = 'app-main'>

        <section className = 'todo-section'>

          <form className = 'todo-form' onSubmit = {addTask}>

            <label className = 'todo-label' htmlFor = 'task-input'>
              New task
            </label>

            <div className = 'todo-input-row'>

              <input id = 'task-input' className = 'todo-input' type = 'text' placeholder = 'Write a TO-DO task' value = {task} onChange = {(e) => setTask(e.target.value)} />

              <button type = 'submit' className = 'todo-button'>
                Add Task
              </button>

            </div>
          </form>

        <section className = 'todo-list-section'>

          <h2 className = 'todo-list-title'>
            Tasks
          </h2>

          {loading && <p> Loading tasks ... </p> }

          <ul className = 'todo-list'>

            {!loading && taskList.length == 0 && (
              <li className = 'todo-empty'> No tasks yet! Add your first task. </li>
            )}

            {taskList.map((task) => (

              <li key = {task.id} className = 'todo-item'>

                <span className = 'todo-text'>
                  {task.text}
                </span>

                <button className = 'todo-delete-button' onClick = {() => deleteTask(task.id)}>
                  Delete
                </button>

              </li>

            ))}

          </ul>
        </section>
        </section>
      </main>
    </div>
);

}


export default App;