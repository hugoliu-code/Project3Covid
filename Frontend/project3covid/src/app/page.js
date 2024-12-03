import Image from "next/image";
import React from "react";
import ApiForm from "./components/apiform";

export default function Home() {
  return (
    <div className="bg-black min-h-screen flex flex-col justify-start mt-12 items-center font-mono">
      <title>Covid Percentile</title>
      <h1 className="text-4xl text-white">Community Covid Safety Percentile</h1>
      <h2 className="text-gray-400 text-center mt-4">
        Find out what percentile of covid danger your community is in <br></br>
        Input your state and county below
      </h2>

      <ApiForm></ApiForm>
    </div>
  );
}
