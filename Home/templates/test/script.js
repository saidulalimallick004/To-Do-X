document.getElementById("addTaskBtn").addEventListener("click", function () {
    let taskText = prompt("Enter a new task:");
    if (taskText) {
        let newTask = document.createElement("li");
        newTask.className = "list-group-item d-flex align-items-center";
        newTask.innerHTML = `<input type="checkbox" class="form-check-input me-2"> ${taskText}`;
        document.getElementById("task-list").appendChild(newTask);
    }
});
