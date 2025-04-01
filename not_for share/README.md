# Kafka and ZooKeeper Integration: Distributed Data Management for AI or Coding

step-by-step guide download, install, and use Apache Kafka

- sending messages with Python producer:
  ![img_2.png](images%2Fimg_2.png)

- receiving messages with Python consumer:
  ![img_3.png](images%2Fimg_3.png)


- sending messages with CMD:
  ![img_1.png](images/img_1.png)

- receiving messages with CMD:
  ![img.png](images%2Fimg.png)

---

### **Step 1: Prerequisites**

Before installing Kafka, ensure that your system meets the following requirements:

1. **Java Development Kit (JDK)**:
    - Kafka requires Java to run. You need to install **JDK 11** or later.
    - Download JDK from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or [OpenJDK](https://openjdk.org/).
    - After installation, verify it by running:
      ```bash
      java -version
      ```
      Ensure the output shows the correct version of Java.

2. **7-Zip** (Optional but recommended):
    - Kafka binaries are distributed as `.tgz` files, which require extraction. Install [7-Zip](https://www.7-zip.org/) to extract the files [[1]].

3. **Notepad++** (Optional):
    - For editing configuration files, you can use Notepad++ or any text editor [[1]].

4. **Windows Subsystem for Linux (WSL2)** (Optional but recommended):
    - If you face issues running Kafka natively on Windows, consider using **WSL2**. It provides a more stable environment for Kafka [[6]].
    - To install WSL2, follow Microsoft's official guide: [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

---

### **Step 2: Download Kafka**

1. Go to the official Apache Kafka website and download the latest binary release:
    - Visit [Kafka Downloads](https://kafka.apache.org/downloads).
    - Under **Binary downloads**, select the **Scala 2.13** version (e.g., `kafka_2.13-3.9.0.tgz`) [[4]].

2. Extract the downloaded `.tgz` file:
    - Use **7-Zip** or any other tool to extract the file into a directory, e.g., `D:\programs\2025\Kafka\kafka_2.13-3.9.0`.

---

### **Step 3: Configure Kafka**

#### **Option A: Using ZooKeeper**

1. **Create Data Directories**:
    - Kafka requires directories to store logs. Create two folders:
        - `D:\programs\2025\Kafka\kafka_2.13-3.9.0\zookeeper-data`
        - `D:\programs\2025\Kafka\kafka_2.13-3.9.0\kafka-logs`

2. **Edit `zookeeper.properties`**:
    - Open the `config/zookeeper.properties` file in your Kafka directory.
    - Update the `dataDir` property to point to the ZooKeeper data directory:
      ```properties
      dataDir=C:/kafka_2.13-3.9.0/zookeeper-data
      ```

3. **Edit `server.properties`**:
    - Open the `config/server.properties` file.
    - Update the `log.dirs` property to point to the Kafka logs directory:
      ```properties
      log.dirs=C:/kafka_2.13-3.9.0/kafka-logs
      ```

4. **Start ZooKeeper**:
    - Open a Command Prompt and navigate to your Kafka directory:
      ```bash
      cd D:\programs\2025\Kafka\kafka_2.13-3.9.0
      ```
    - Start ZooKeeper:
      ```bash
      .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
      ```

5. **Start Kafka Broker**:
    - Open another Command Prompt and navigate to your Kafka directory.
    - Start the Kafka broker:
      ```bash
      .\bin\windows\kafka-server-start.bat .\config\server.properties
      ```

#### **Option B: Using KRaft Mode**

1. **Generate Cluster ID**:
    - In KRaft mode, Kafka does not rely on ZooKeeper. First, generate a cluster ID:
      ```bash
      .\bin\windows\kafka-storage.bat random-uuid
      ```
    - Copy the generated UUID.

2. **Format Storage**:
    - Format the storage directory with the cluster ID:
      ```bash
      .\bin\windows\kafka-storage.bat format -t <CLUSTER_ID> -c .\config\kraft\server.properties
      ```

3. **Start Kafka Broker**:
    - Start the Kafka broker in KRaft mode:
      ```bash
      .\bin\windows\kafka-server-start.bat .\config\kraft\server.properties
      ```

---

### **Step 4: Test Kafka**

```bash
      cd D:\kafka_2.13-3.9.0
```

1. **Create a Topic**:
    - Open a new Command Prompt and create a topic:
      ```bash
      .\bin\windows\kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
      ```

this Created topic test-topic.

2. **Produce Messages**:
    - Start a producer to send messages:
      ```bash
      .\bin\windows\kafka-console-producer.bat --topic test-topic --bootstrap-server localhost:9092
      ```
    - Type messages in the console and press Enter to send them.
    - Type message 1 in the console and press Enter to send them
    - Type message 2 in the console and press Enter to send them

3. **Consume Messages**:
    - Open another Command Prompt and start a consumer to read messages:
      ```bash
      .\bin\windows\kafka-console-consumer.bat --topic test-topic --from-beginning --bootstrap-server localhost:9092
      ```
      this will receive all the messages that have been sent

---

### **Step 5: Use Kafka with Python**

**Run the Scripts**:

- Start the producer:
  ```bash 
  python producer_is_sending_message_to_Kafka_with_Python.py
  ```
- Start the consumer:
  ```bash
  python consumer_is_getting_message_to_Kafka_with_Python.py
  ```
