Great! Since you've completed **Step 2** (downloading Kafka), let's move on to setting up and using **ZooKeeper** for your Kafka installation. ZooKeeper is traditionally used by Kafka for cluster coordination, leader election, and metadata management [[2]]. Although Kafka 3.9.0 supports **KRaft mode** (which eliminates the need for ZooKeeper), we'll focus on using ZooKeeper as per your preference.

Here’s a step-by-step guide to set up and use ZooKeeper with Kafka:

---

### **Step 1: Create Required Directories**

Before starting ZooKeeper, you need to create directories where ZooKeeper will store its data.

1. Navigate to your Kafka directory:
   ```bash
   cd D:\kafka_2.13-3.9.0
   ```

2. Create a folder for ZooKeeper data:
   ```bash
   mkdir zookeeper-data
   ```

---

### **Step 2: Configure `zookeeper.properties`**

The `zookeeper.properties` file contains the configuration settings for ZooKeeper.

1. Open the `config/zookeeper.properties` file in a text editor (e.g., Notepad++):
   ```bash
   notepad config\zookeeper.properties
   ```

2. Update the `dataDir` property to point to the directory you just created:
   ```properties
   dataDir=C:/kafka_2.13-3.9.0/zookeeper-data
   ```

   This tells ZooKeeper where to store its data files [[4]].

---

### **Step 3: Start ZooKeeper**

Once the configuration is complete, you can start the ZooKeeper server.

1. Open a **Command Prompt** and navigate to your Kafka directory:
   ```bash
   cd D:\kafka_2.13-3.9.0
   ```

2. Start ZooKeeper using the following command:
   ```bash
   .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
   ```

    - If everything is set up correctly, you should see logs indicating that ZooKeeper has started successfully.
    - ZooKeeper will listen on port `2181` by default [[9]].

---

### **Step 4: Verify ZooKeeper**

To confirm that ZooKeeper is running properly, you can connect to it using the `zkCli` tool (ZooKeeper Command Line Interface).

1. Open a new **Command Prompt** and run the following command:
   ```bash
   .\bin\windows\zkCli.bat
   ```

2. Once connected, you can issue commands like:
   ```bash
   ls /
   ```
   This lists the root nodes in ZooKeeper. If you see output like `[zookeeper]`, ZooKeeper is working correctly [[4]].

---

### **Step 5: Configure Kafka to Use ZooKeeper**

Now that ZooKeeper is running, you need to configure Kafka to connect to it.

1. Open the `config/server.properties` file in a text editor:
   ```bash
   notepad config\server.properties
   ```

2. Ensure the following properties are set:
   ```properties
   zookeeper.connect=localhost:2181
   log.dirs=C:/kafka_2.13-3.9.0/kafka-logs
   ```

    - The `zookeeper.connect` property tells Kafka where to find the ZooKeeper instance.
    - The `log.dirs` property specifies where Kafka will store its log files [[9]].

---

### **Step 6: Start Kafka Broker**

With ZooKeeper running, you can now start the Kafka broker.

1. Open a new **Command Prompt** and navigate to your Kafka directory:
   ```bash
   cd D:\kafka_2.13-3.9.0
   ```

2. Start the Kafka broker using the following command:
   ```bash
   .\bin\windows\kafka-server-start.bat .\config\server.properties
   ```

    - If everything is configured correctly, you should see logs indicating that the Kafka broker has started successfully.
    - Kafka will listen on port `9092` by default [[9]].

---

### **Step 7: Test Kafka with ZooKeeper**

Now that both ZooKeeper and Kafka are running, you can test the setup by creating a topic, producing messages, and consuming them.

1. **Create a Topic**:
    - Open a new **Command Prompt** and run:
      ```bash
      .\bin\windows\kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
      ```

2. **Produce Messages**:
    - Start a producer to send messages:
      ```bash
      .\bin\windows\kafka-console-producer.bat --topic test-topic --bootstrap-server localhost:9092
      ```
    - Type messages in the console and press Enter to send them.

3. **Consume Messages**:
    - Open another **Command Prompt** and start a consumer to read messages:
      ```bash
      .\bin\windows\kafka-console-consumer.bat --topic test-topic --from-beginning --bootstrap-server localhost:9092
      ```

    - You should see the messages you sent being consumed in real-time.

---

### **Optional: Run ZooKeeper as a Windows Service**

If you want ZooKeeper to run in the background as a Windows service, you can configure it using tools like **NSSM (Non-Sucking Service Manager)** or by modifying the `zkServer.cmd` script [[10]].

---

### **Troubleshooting Tips**

1. **Port Conflicts**:
    - Ensure that ports `2181` (ZooKeeper) and `9092` (Kafka) are not being used by other applications.

2. **Firewall/Antivirus**:
    - Disable your firewall or antivirus temporarily if they block ZooKeeper or Kafka processes.

3. **WMIC Issues**:
    - If you encounter an error like `'wmic' is not recognized`, consider upgrading to a newer version of Windows or using WSL2 [[5]].

---

By following these steps, you should have a fully functional Kafka setup using ZooKeeper on Windows. If you encounter any issues or need further clarification, feel free to ask!

old:

---

### **Troubleshooting Tips**

1. **WMIC Issues**:
    - If you encounter an error like `'wmic' is not recognized`, it may be due to the deprecation of `wmic` in newer Windows versions. Consider using WSL2 or manually setting up the environment variables [[5]].

2. **Port Conflicts**:
    - Ensure that ports `9092` (Kafka) and `2181` (ZooKeeper) are not being used by other applications.

3. **Firewall/Antivirus**:
    - Disable your firewall or antivirus temporarily if they block Kafka processes.

---

By following these steps, you should be able to successfully set up and use Kafka on Windows. If you encounter any specific issues, feel free to ask for further assistance!