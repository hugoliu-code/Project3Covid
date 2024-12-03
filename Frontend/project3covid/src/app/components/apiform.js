"use client";

import React, { useState } from "react";

const states = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Delaware",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illinois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming",
];

export default function ApiForm() {
  const [dropdownValue, setDropdownValue] = useState("");
  const [textValue, setTextValue] = useState("");
  const [response, setResponse] = useState(null);

  const handleSubmit = async () => {
    if (!dropdownValue || !textValue.trim()) {
      alert("Please fill out all fields.");
      return;
    }

    try {
      const res = await fetch("/api/endpoint", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          state: dropdownValue,
          input: textValue,
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to send request");
      }

      const data = await res.json();
      setResponse(data.message); // Adjust based on your API response structure
    } catch (error) {
      console.error("Error:", error);
      setResponse("Something went wrong. Please try again.");
    }
  };

  return (
    <div class="flex flex-col">
      <div class="space-x-4 flex mt-4">
        <select
          type="text"
          className="border p-2 w-full text-gray-400"
          placeholder="State"
          onChange={(e) => setDropdownValue(e.target.value)}
        >
          <option value="" disabled default>
            state
          </option>
          {states.map((state) => (
            <option key={state} value={state}>
              {state}
            </option>
          ))}
        </select>
        <input
          type="text"
          className="border p-2 w-full text-gray-400"
          placeholder="County"
          onChange={(e) => setTextValue(e.target.value)}
        />

        <button
          onClick={handleSubmit}
          className="bg-blue-500 text-gray-400 py-2 px-4 rounded hover:bg-blue-600"
        >
          Submit
        </button>
      </div>
      {response && (
        <div className="mt-4 p-4">
          <strong className="text-gray-200">Percentile:</strong> {response}
        </div>
      )}
    </div>
  );
}
