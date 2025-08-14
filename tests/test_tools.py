#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eğitim Paint Uygulaması - Tools Modülü Testleri
Bu dosya, tools.py modülündeki Tool sınıfını test eder
"""

import unittest
import sys
import os

# demo1 klasörünü Python path'ine ekle
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'demo1'))

from tools import Tool


class TestTool(unittest.TestCase):
    """Tool sınıfı için test sınıfı"""

    def setUp(self):
        """Her test öncesi çalışır"""
        self.tool = Tool("TestTool", "Test")

    def test_tool_creation(self):
        """Tool oluşturma testi"""
        self.assertEqual(self.tool.name, "TestTool")
        self.assertEqual(self.tool.type, "Test")

    def test_tool_attributes(self):
        """Tool özelliklerinin doğru ayarlandığını test eder"""
        tool = Tool("Kalem", "Çizim")
        self.assertEqual(tool.name, "Kalem")
        self.assertEqual(tool.type, "Çizim")

    def test_tool_string_representation(self):
        """Tool string temsilini test eder"""
        tool = Tool("Fırça", "Çizim")
        expected = "Tool(name='Fırça', type='Çizim')"
        self.assertEqual(str(tool), expected)

    def test_tool_repr(self):
        """Tool repr metodunu test eder"""
        tool = Tool("Silgi", "Silme")
        expected = "Tool(name='Silgi', type='Silme')"
        self.assertEqual(repr(tool), expected)

    def test_tool_equality(self):
        """Tool eşitlik karşılaştırmasını test eder"""
        tool1 = Tool("Araç1", "Tip1")
        tool2 = Tool("Araç1", "Tip1")
        tool3 = Tool("Araç2", "Tip1")
        
        self.assertEqual(tool1, tool2)
        self.assertNotEqual(tool1, tool3)

    def test_tool_hash(self):
        """Tool hash değerini test eder"""
        tool1 = Tool("Araç1", "Tip1")
        tool2 = Tool("Araç1", "Tip1")
        
        self.assertEqual(hash(tool1), hash(tool2))

    def test_tool_with_empty_strings(self):
        """Boş string'lerle Tool oluşturmayı test eder"""
        tool = Tool("", "")
        self.assertEqual(tool.name, "")
        self.assertEqual(tool.type, "")

    def test_tool_with_special_characters(self):
        """Özel karakterlerle Tool oluşturmayı test eder"""
        tool = Tool("Araç-Özel_123", "Tip-Özel_123")
        self.assertEqual(tool.name, "Araç-Özel_123")
        self.assertEqual(tool.type, "Tip-Özel_123")


class TestToolIntegration(unittest.TestCase):
    """Tool sınıfının entegrasyon testleri"""

    def test_multiple_tools(self):
        """Birden fazla Tool oluşturmayı test eder"""
        tools = [
            Tool("Kalem", "Çizim"),
            Tool("Fırça", "Çizim"),
            Tool("Silgi", "Silme"),
            Tool("Şekil", "Şekil")
        ]
        
        self.assertEqual(len(tools), 4)
        self.assertEqual(tools[0].name, "Kalem")
        self.assertEqual(tools[1].type, "Çizim")
        self.assertEqual(tools[2].name, "Silgi")
        self.assertEqual(tools[3].type, "Şekil")

    def test_tool_in_list(self):
        """Tool'ların listelerde kullanımını test eder"""
        tool = Tool("TestTool", "Test")
        tool_list = [tool]
        
        self.assertIn(tool, tool_list)
        self.assertEqual(tool_list[0].name, "TestTool")

    def test_tool_as_dict_key(self):
        """Tool'ların dictionary key olarak kullanımını test eder"""
        tool1 = Tool("Key1", "Type1")
        tool2 = Tool("Key2", "Type2")
        
        tool_dict = {tool1: "Value1", tool2: "Value2"}
        
        self.assertEqual(tool_dict[tool1], "Value1")
        self.assertEqual(tool_dict[tool2], "Value2")


if __name__ == '__main__':
    # Test suite'i oluştur
    test_suite = unittest.TestSuite()
    
    # Test sınıflarını ekle
    test_suite.addTest(unittest.makeSuite(TestTool))
    test_suite.addTest(unittest.makeSuite(TestToolIntegration))
    
    # Test runner'ı çalıştır
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Test sonuçlarını yazdır
    print(f"\n{'='*50}")
    print(f"Test Sonuçları:")
    print(f"Çalıştırılan: {result.testsRun}")
    print(f"Başarılı: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Başarısız: {len(result.failures)}")
    print(f"Hatalı: {len(result.errors)}")
    print(f"{'='*50}")
    
    # Exit code'u ayarla
    sys.exit(len(result.failures) + len(result.errors))
