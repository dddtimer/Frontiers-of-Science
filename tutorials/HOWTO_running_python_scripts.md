### **Quick Start Guide: Running the Python Scripts for Argos Lessons**

This guide provides step-by-step instructions for future instructions on how to set up their environment and run the Python scripts associated with the Argos lessons.

---

#### **1. Install Python via Miniconda**

Miniconda is a minimal installer for conda, a package and environment management system that makes it easy to install Python and necessary packages.

**Steps:**

1. **Download Miniconda:**

   - Visit the [Miniconda Download Page](https://docs.conda.io/en/latest/miniconda.html).
   - Choose the appropriate installer for your operating system (Windows, macOS, or Linux) and your system architecture (64-bit or 32-bit).

2. **Install Miniconda:**

   - Run the downloaded installer.
   - Follow the installation prompts.
     - **For Windows Users:** You may be prompted to add Miniconda to your PATH environment variable. It's recommended to select this option.
     - **For macOS/Linux Users:** Follow the terminal prompts.

---

#### **2. Set Up a Conda Environment**

Creating a separate environment helps manage dependencies without affecting other Python projects.

**Steps:**

1. **Open a Terminal or Command Prompt.**

2. **Create a New Environment Named `argos_env`:**

   ```bash
   conda create -n argos_env python=3.11
   ```

   - This command creates a new environment with Python 3.11 installed.

3. **Activate the Environment:**

   ```bash
   conda activate argos_env
   ```

---

#### **3. Install Necessary Packages**

The scripts require specific Python packages. Install them using `conda` or `pip`.

**Steps:**

1. **Install Packages Using Conda:**

   ```bash
   conda install numpy matplotlib scipy pandas
   ```

   - These packages are:
     - `numpy`: For numerical computations.
     - `matplotlib`: For plotting graphs and figures.
     - `scipy`: For advanced mathematical functions.
     - `pandas`: For data manipulation.

2. **Alternatively, Install Packages Using Pip:**

   ```bash
   pip install numpy matplotlib scipy pandas
   ```

---

#### **4. Clone the GitHub Repository**

Retrieve the scripts from the GitHub repository where they are stored.

**Steps:**

1. **Ensure Git is Installed:**

   - **Windows Users:** Download from [git-scm.com](https://git-scm.com/download/win).
   - **macOS Users:** Git is usually pre-installed. If not, install via Homebrew (`brew install git`) or download from [git-scm.com](https://git-scm.com/download/mac).
   - **Linux Users:** Install via your package manager, e.g., `sudo apt-get install git`.

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/argos-lessons.git
   ```

   - Replace `https://github.com/yourusername/argos-lessons.git` with the actual repository URL.

3. **Navigate to the Repository Directory:**

   ```bash
   cd argos-lessons
   ```

---

#### **5. Running the Scripts**

Now you're ready to run the Python scripts.

**Steps:**

1. **Ensure the Conda Environment is Active:**

   ```bash
   conda activate argos_env
   ```

2. **Run a Python Script:**

   ```bash
   python L1_S6_Fig1-W_histogram_subject2.py
   ```

   - Replace `L1_S6_Fig1-W_histogram_subject2.py` with the name of the script you wish to run.

3. **View the Output:**

   - The script will generate figures and save them as PNG files in the same directory.
   - Plots will also display in a window if running in an environment that supports GUI.

---

#### **6. Additional Notes**

- **Updating Packages:**

  - To update all packages to their latest versions:

    ```bash
    conda update --all
    ```

- **Deactivating the Environment:**

  - When finished, you can deactivate the environment:

    ```bash
    conda deactivate
    ```

- **Running Scripts in an IDE:**

  - You can also run these scripts using an Integrated Development Environment (IDE) like VSCode or PyCharm. Ensure the IDE is configured to use the `argos_env` environment.

---

#### **7. Troubleshooting**

- **Common Issues:**

  - *Module Not Found Errors:* Ensure all required packages are installed in the `argos_env` environment.
  - *Environment Activation Issues:* Verify that the environment is activated before running scripts.

- **Checking Installed Packages:**

  ```bash
  conda list
  ```

  - This command lists all packages installed in the active environment.

- **Environment Information:**

  ```bash
  conda info
  ```

---

