import Logo from "../iconComponents/Logo";  // ← use a capitalized import

export default function Header() {
  return (
    <header className="flex items-center p-4 pl-0 bg-Header border-b-2 border-Border place-content-center  lg:place-content-start ">
      <Logo className="w-75 h-26" />
    </header>
  );
}