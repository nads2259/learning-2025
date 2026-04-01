import React , {useState} from 'react';
import './Login.css';

const AUTH = 'http://localhost:5000/api'

function Login({onLogin})
{
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
    const [confirmPassword,setConfirmPassword] = useState('');
    const [mode,setMode] = useState('login');
    const [error,setError] = useState('');

    async function handleSubmit(event)
    {
        event.preventDefault();
        setError('');

        if (!email | !password)
        {
            setError('Email and password are required!');
            return;
        }
        
        if (mode === 'register' & confirmPassword !== password)
        {
            setError('Passwords do not match!');
            return;
        }

        try 
        {
            const endpoint = (mode === 'register') ? `${AUTH}/register` : `${AUTH}/login`;

            const response = await fetch(endpoint,
                {
                    method : 'POST',
                    headers : {'Content-Type' : 'application/json'},
                    body : JSON.stringify({email,password}),
                }
            );

            const data = await response.json();

            if (!response.ok)
            {
                setError(data.error);
                return;
            }

            onLogin(data.token);
            setEmail('');
            setPassword('');
            setConfirmPassword('');
        } catch (err)
        {
            console.error(err);
        }
        
    }

    function toggleMode()
    {
        setMode((prev) => (prev === 'login' ? 'register' : 'login'));
    }

    const isRegister = (mode === 'register');


return (

    <div className = 'auth-container'>
        
        <div className = 'auth-card'>
            
            <h2 className = 'auth-title'> {isRegister ? 'Create an account' : 'Login'} </h2>

            {error && (
                <p className = 'auth-error'> {error} </p>
            )}

            <form className = 'auth-form' onSubmit = {handleSubmit}>

                <label className = 'auth-label'> Email </label>

                <input className = 'auth-input' type = 'email' placeholder = 'you@example.com' value = {email} onChange = {(e) => setEmail(e.target.value)} />

                <label className = 'auth-label'> Password </label>

                <input className = 'auth-input' type = 'password' placeholder = 'Enter password' value = {password} onChange = {(e) => setPassword(e.target.value)} />

                {isRegister && (
                    <>
                        <label className = 'auth-label'> Confirm password </label>
                        
                        <input className = 'auth-input' type = 'password' placeholder = 'Re-enter password' value = {confirmPassword} onChange = {(e) => setConfirmPassword(e.target.value)} />
                    </>
                )}

                <button className = 'auth-button' type = 'submit'> {isRegister ? 'Register' : 'Log In'} </button>
            </form>

            <p className = 'auth-toggle-text'>
                {isRegister ? 'Already have an account ?' : 'Don"t have an account'}
                <span className = 'auth-toggle-link' onClick = {toggleMode}>
                    {isRegister ? 'Log In' : 'Register'}
                </span>
            </p>
        </div>

    </div>

)
}

export default Login;