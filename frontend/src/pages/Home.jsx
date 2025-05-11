import Header from "../components/Header"

function Home(){
    return (
        <div>
        <Header />

            <div className="flex ">
            <aside className="sticky top-0 w-38 p-4 bg-Components border-2
             border-Border_secondary flex flex-col items-center text-center lg:h-screen lg:w-84 ">
                <div className="my-64 lg:mt-64">
                <nav className="space-y-4">
                    <a href="/excelupload" className="block">Import Excel Sheet</a>
                </nav>
                </div>
                
            </aside>
                <main className="flex-1 p-4  bg-Mainbg flex items-center justify-center  lg:min-h-screen">
                    <div className="p-6 bg-Components rounded shadow max-w-lg text-center border-2 border-Border">
                        <h2 className="text-2xl font-semibold mb-2">Demo Lab Site</h2>
                        <p>Enter our main ideas and other stuff lol</p>
                    </div>
                </main>
            </div>
        </div>

    )
}
export default Home
