"""
Basic tests for astrology calculations
"""

import unittest
from datetime import datetime
from core.birth_data import BirthData
from calculations.sun_moon_signs import calculate_sun_moon_signs, get_sun_moon_compatibility
from calculations.lagna import calculate_lagna, calculate_lagna_lord
from calculations.dasha import calculate_vimshottari_dasha

class TestAstrologyCalculations(unittest.TestCase):
    """Test cases for astrology calculations"""
    
    def setUp(self):
        """Set up test data"""
        self.birth_data = BirthData(
            date="1990-05-15",
            time="14:30",
            latitude=28.6139,  # Delhi
            longitude=77.2090,
            name="Test Person"
        )
    
    def test_birth_data_creation(self):
        """Test BirthData creation"""
        self.assertEqual(self.birth_data.date.year, 1990)
        self.assertEqual(self.birth_data.date.month, 5)
        self.assertEqual(self.birth_data.date.day, 15)
        self.assertEqual(self.birth_data.time.hour, 14)
        self.assertEqual(self.birth_data.time.minute, 30)
        self.assertEqual(self.birth_data.latitude, 28.6139)
        self.assertEqual(self.birth_data.longitude, 77.2090)
        self.assertEqual(self.birth_data.name, "Test Person")
    
    def test_sun_moon_calculation(self):
        """Test Sun and Moon sign calculations"""
        sun_moon_data = calculate_sun_moon_signs(self.birth_data)
        
        # Check that we get valid data
        self.assertIn('sun_sign', sun_moon_data)
        self.assertIn('moon_sign', sun_moon_data)
        self.assertIn('birth_data', sun_moon_data)
        
        sun_sign = sun_moon_data['sun_sign']
        moon_sign = sun_moon_data['moon_sign']
        
        # Check required fields
        self.assertIn('sign', sun_sign)
        self.assertIn('degree', sun_sign)
        self.assertIn('formatted_degree', sun_sign)
        self.assertIn('element', sun_sign)
        self.assertIn('quality', sun_sign)
        
        self.assertIn('sign', moon_sign)
        self.assertIn('degree', moon_sign)
        self.assertIn('formatted_degree', moon_sign)
        self.assertIn('element', moon_sign)
        self.assertIn('quality', moon_sign)
        
        # Check that signs are valid
        valid_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                      'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
        
        self.assertIn(sun_sign['sign'], valid_signs)
        self.assertIn(moon_sign['sign'], valid_signs)
    
    def test_lagna_calculation(self):
        """Test Lagna calculations"""
        lagna_data = calculate_lagna(self.birth_data)
        
        # Check that we get valid data
        self.assertIn('lagna_sign', lagna_data)
        self.assertIn('lagna_degree', lagna_data)
        self.assertIn('formatted_degree', lagna_data)
        self.assertIn('element', lagna_data)
        self.assertIn('quality', lagna_data)
        
        # Check that lagna sign is valid
        valid_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                      'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
        
        self.assertIn(lagna_data['lagna_sign'], valid_signs)
        
        # Check degree range
        self.assertGreaterEqual(lagna_data['lagna_degree'], 0)
        self.assertLess(lagna_data['lagna_degree'], 360)
    
    def test_lagna_lord_calculation(self):
        """Test Lagna Lord calculations"""
        lagna_lord_data = calculate_lagna_lord(self.birth_data)
        
        # Check that we get valid data
        self.assertIn('lagna_sign', lagna_lord_data)
        self.assertIn('lagna_lord', lagna_lord_data)
        
        # Check that lagna lord is a valid planet
        valid_planets = ['SUN', 'MOON', 'MARS', 'VENUS', 'MERCURY', 'JUPITER', 'SATURN']
        self.assertIn(lagna_lord_data['lagna_lord'], valid_planets)
    
    def test_dasha_calculation(self):
        """Test Dasha calculations"""
        dasha_data = calculate_vimshottari_dasha(self.birth_data)
        
        # Check that we get valid data
        self.assertIn('birth_nakshatra', dasha_data)
        self.assertIn('birth_dasha_lord', dasha_data)
        self.assertIn('dasha_periods', dasha_data)
        
        # Check that birth nakshatra is valid
        valid_nakshatras = [
            'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
            'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni', 'Uttara Phalguni',
            'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha', 'Jyeshtha',
            'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishta', 'Shatabhisha',
            'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
        ]
        
        self.assertIn(dasha_data['birth_nakshatra'], valid_nakshatras)
        
        # Check that we have dasha periods
        self.assertIsInstance(dasha_data['dasha_periods'], list)
        self.assertGreater(len(dasha_data['dasha_periods']), 0)
    
    def test_compatibility_calculation(self):
        """Test Sun-Moon compatibility calculations"""
        compatibility_data = get_sun_moon_compatibility(self.birth_data)
        
        # Check that we get valid data
        self.assertIn('sun_sign', compatibility_data)
        self.assertIn('moon_sign', compatibility_data)
        self.assertIn('compatibility_score', compatibility_data)
        self.assertIn('interpretation', compatibility_data)
        
        # Check compatibility score range
        self.assertGreaterEqual(compatibility_data['compatibility_score'], 0)
        self.assertLessEqual(compatibility_data['compatibility_score'], 1)
    
    def test_invalid_birth_data(self):
        """Test handling of invalid birth data"""
        # Test invalid latitude
        with self.assertRaises(ValueError):
            BirthData(
                date="1990-05-15",
                time="14:30",
                latitude=100,  # Invalid latitude
                longitude=77.2090
            )
        
        # Test invalid longitude
        with self.assertRaises(ValueError):
            BirthData(
                date="1990-05-15",
                time="14:30",
                latitude=28.6139,
                longitude=200  # Invalid longitude
            )
        
        # Test future date
        with self.assertRaises(ValueError):
            BirthData(
                date="2030-05-15",  # Future date
                time="14:30",
                latitude=28.6139,
                longitude=77.2090
            )

if __name__ == '__main__':
    unittest.main() 