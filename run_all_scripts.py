import subprocess

def run_script(script_name):
    print(f"Running {script_name}...")
    subprocess.run(["python", script_name], check=True)

if __name__ == "__main__":
    scripts = [
        "revenue_for_each_month.py",
        "revenue_from_each_product.py",
        "revenue_from_each_customer.py",
        "top_10_customers.py"
    ]
    
    for script in scripts:
        run_script(script)
