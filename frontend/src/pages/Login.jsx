import Form from "../components/Form"
import Header from "../components/Header"
function Login() {
    return(
        <div>
            <Header></Header>
        <div className="text-white bg-Mainbg min-h-screen flex items-center justify-center ">
        <div className="w-full max-w-md px-4 ">
            <div className="bg-Components border-1 border-Border_secondary">
                <Form route="/api/token/" method="login" />
            </div>
        </div>
        </div>
        </div>
  )
}

export default Login