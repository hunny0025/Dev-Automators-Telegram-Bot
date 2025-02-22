# **Contribution Guidelines for Dev-Automators-Telegram-Bot**  

Welcome to **Dev-Automators-Telegram-Bot**! 🎉 We appreciate your interest in enhancing the bot. This document outlines how you can contribute by adding new commands while ensuring consistency and professionalism.  

---  

## **How to Add a New Command**  

### **1. Locate the Command Handling Section**  

Open the source code file where the bot processes commands (e.g., `long-polling.py` or `webhook.py`). Look for the comment:  

```python
# Add your command in this block using elif
```

---

### **2. Follow the Example Format**  

#### **Existing Command Block Example:**  

```python
# Add your command in this block using elif
if message and message.get("text", "").strip() == "/start":
    greeting = random.choice(greetings)
    send_message(chat_id, greeting)
else:
    send_message(chat_id, "Invalid message")
```  

#### **How to Add a New Command:**  

```python
# Add your command in this block using elif 
if message.get("text", "").strip() == "/start":
    greeting = random.choice(greetings)
    send_message(chat_id, greeting)
elif message.get("text", "").strip() == "/help":
    send_message(chat_id, "Here are the available commands:\n/start - Greet the user\n/help - Show available commands")
else:
    send_message(chat_id, "Invalid command. Use /help for assistance.")
```  

---

### **3. Command Contribution Guidelines**  

✅ **Use the Correct Format:** Follow the structure above for consistency.  
✅ **Keep It Professional:** Ensure the responses are appropriate, respectful, and free from slang.  
✅ **Test Your Command:** Verify that your new command works and does not break existing functionality.  
✅ **Document Your Changes:** Clearly state what command you added in your commit message.  

---

## **Contribution Workflow**  

### **1. Fork & Clone the Repository**  
Fork the repository from [here](https://github.com/adarshkr357/Dev-Automators-Telegram-Bot). Then, clone it to your local machine:  

```bash
git clone https://github.com/<your-username>/Dev-Automators-Telegram-Bot.git
cd Dev-Automators-Telegram-Bot
```  

### **2. Create a New Branch**  
Always work on a separate branch for new features:  

```bash
git checkout -b add-new-command
```  

### **3. Modify the Code**  
- Add your new command in the designated section following the correct format.  
- Test your command to ensure it works properly.  

### **4. Commit and Push Your Changes**  

```bash
git add .
git commit -m "Added new command: [Your Command Name] -> by [Your Name] - [Your Roll Number]"
git push origin add-new-command
```  

### **5. Submit a Pull Request**  
- Go to your fork on GitHub and open a pull request (PR) to merge your changes into the main repository.  
- Add a short description of your new command in the PR.  

---

## **Important Reminders**  

⚠ **Do NOT remove or modify any existing commands unless necessary.**  
⚠ **Ensure your command follows the bot's purpose and remains professional.**  
⚠ **If you have questions, feel free to ask in the group!**  

Thank you for contributing and helping improve our bot! 🚀