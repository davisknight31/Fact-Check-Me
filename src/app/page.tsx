"use server";
import Image from "next/image";
import LinkInput from "./components/LinkInput";
import Button from "./components/Button";

export default async function Home() {
  const print = () => {
    "use server";
    console.log("hist");
  };
  return (
    <main className="flex min-h-screen flex-col items-center  p-24">
      <h1 className="text-4xl">Fact Check Me</h1>
      <LinkInput></LinkInput>
      <Button label="Begin" handleClick={print}></Button>
    </main>
  );
}
