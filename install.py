"""
Installation script for Astrology Calculation Engine
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing dependencies: {e}")
        return False

def test_swiss_ephemeris():
    """Test Swiss Ephemeris installation"""
    print("Testing Swiss Ephemeris...")
    
    try:
        import swisseph
        print("✓ Swiss Ephemeris imported successfully!")
        return True
    except ImportError as e:
        print(f"✗ Error importing Swiss Ephemeris: {e}")
        print("Please make sure swisseph is installed correctly.")
        return False

def run_basic_test():
    """Run a basic test to verify installation"""
    print("Running basic test...")
    
    try:
        from core.birth_data import BirthData
        from calculations.sun_moon_signs import calculate_sun_moon_signs
        
        # Create test birth data
        birth_data = BirthData(
            date="1990-05-15",
            time="14:30",
            latitude=28.6139,
            longitude=77.2090
        )
        
        # Test calculation
        result = calculate_sun_moon_signs(birth_data)
        
        if 'sun_sign' in result and 'moon_sign' in result:
            print("✓ Basic calculation test passed!")
            print(f"  Sun Sign: {result['sun_sign']['sign']}")
            print(f"  Moon Sign: {result['moon_sign']['sign']}")
            return True
        else:
            print("✗ Basic calculation test failed!")
            return False
            
    except Exception as e:
        print(f"✗ Error in basic test: {e}")
        return False

def main():
    """Main installation function"""
    print("=== Astrology Calculation Engine Installation ===")
    print()
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("✗ Python 3.7 or higher is required!")
        return False
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Test Swiss Ephemeris
    if not test_swiss_ephemeris():
        return False
    
    # Run basic test
    if not run_basic_test():
        return False
    
    print()
    print("=== Installation Complete! ===")
    print()
    print("You can now use the astrology engine:")
    print("  python main.py                    # Run demo")
    print("  python main.py --help            # See command line options")
    print("  python -m pytest tests/          # Run tests")
    print()
    print("Example usage:")
    print("  python main.py --date 1990-05-15 --time 14:30 --latitude 28.6139 --longitude 77.2090")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 