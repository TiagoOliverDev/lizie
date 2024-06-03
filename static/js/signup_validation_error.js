document.getElementById('signupForm').addEventListener('input', function() {
    var password = document.querySelector('input[name="password1"]');
    var confirmPassword = document.querySelector('input[name="password2"]');
    var mismatchMessage = document.getElementById('passwordMismatch');
    
    if (password.value === confirmPassword.value) {
      mismatchMessage.style.display = 'none';
    } else {
      mismatchMessage.style.display = 'block';
    }
});