🎯 External Sort Visualizer

1. Project Description

The External Sort Visualizer is an educational project that visually demonstrates the operation of the external sorting algorithm using a min-heap. The project is intended for students and developers studying algorithms and data structures.

2. Main features:
- 📊 Real-time visualization of the sorting process
- 🎲 Generation of random data for demonstration
- 🔢 Two modes of operation: with a graphical interface and console
- 📈 Step-by-step animation of the algorithm

3. Installation and launch

3.3 Requirements
- Python 3.8+
- pip (package manager)

4. Installation steps

4.4 Clone the repository:
```
git clone https://github.com/sadfyuii/outsorting-method-heaps-chunks-.git
cd outsorting-method-heaps-chunks-

pip install -r requirements.txt
bash

python outsort.py
```

## 🛠️ Technical Requirements

### 💻 System Requirements
- **Programming language:** Python 3.8+
- **Operating systems:** Windows 10+, Linux Ubuntu 18.04+, macOS 10.14+

### 📦 Key Dependencies
python
matplotlib >= 3.5.0    # Data visualization and plotting
numpy >= 1.21.0        # Numerical computations and array handling


## 🔄 Algorithm of Operation

### 📋 Step-by-Step Process

1. **🎲 Data Generation** 
   - Creating a random array of numbers for sorting demonstration
   - Configurable array size and value range

2. **📦 Chunking Phase** 
   - Splitting the data into manageable sorted blocks
   - Each chunk is sorted individually using internal sorting
   - Configurable chunk size based on available memory

3. **🏗️ Heap Construction** 
   - Initializing the min-heap with the first elements of each chunk
   - Creating a priority queue for efficient minimum element extraction
   - Maintaining chunk references for sequential element access

4. **🔄 Merging Phase** 
   - Sequentially extracting the minimum elements from the heap
   - Adding extracted elements to the resulting sorted array
   - Replenishing the heap with next elements from respective chunks
   - Continuing until all chunks are fully processed

### 🎯 Algorithm Characteristics
- **⏱️ Time Complexity:** O(n log k) where k is the number of chunks
- **💾 Space Complexity:** O(k) for the heap structure
- **⚖️ Stability:** Maintains relative order of equal elements
- **🚀 Efficiency:** Optimal for large datasets that don't fit in memory


## 👤 Authors

### 🎓 Project Lead & Developer
**Grinev Makar Dmitrievich**  
📧 Email: [pmdworking@yandex.ru](mailto:pmdworking@yandex.ru)  
🎯 Roles: 
- 🧠 Algorithm Developer
- 🏗️ Project Architect  
- 📊 Visualization Developer
- 📝 Technical Writer
- 🧪 Tester

## 📞 Feedback

### 🔧 Support Channels
- **📧 Email:** [feedback@external-sort.com](mailto:feedback@external-sort.com)
- **🐛 Bugs and Suggestions:** [GitHub Issues](/Issues)
- **💬 Discussions:** [GitHub Discussions](/Discussions)

