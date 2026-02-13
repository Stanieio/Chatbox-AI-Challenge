const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

// Test route
app.get("/", (req, res) => {
  res.send("Node server is working");
});

// Chat route
app.post("/chat", async (req, res) => {
  try {
    const { message } = req.body;

    const response = await axios.post(
      "http://127.0.0.1:8000/ai",
      { message }
    );

    res.json({ reply: response.data.reply });

  } catch (error) {
    console.error("ERROR:", error.message);
    res.status(500).json({ error: "Node server error" });
  }
});

app.listen(5000, () => {
  console.log("🚀 Node server running on port 5000");
});
