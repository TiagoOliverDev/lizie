function checkCompletionStatus() {
    const isCompleted = document.getElementById('is-completed').value === 'true';
    if (isCompleted) {
      alert("Cannot delete a completed task.");
      return false; 
    }
    return true; 
}