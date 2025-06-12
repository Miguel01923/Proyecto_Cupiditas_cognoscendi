#!/usr/bin/env python3
"""
Sistema de Aprendizaje Adaptativo - Versión Extendida
Diseñado para enseñar desde CERO hasta nivel EXPERTO
Con explicaciones súper claras y ejemplos del mundo real
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import random
import time

class SistemaAprendizajeCompleto:
    def __init__(self):
        self.usuarios = {}
        self.modulos = self._crear_temario_completo()
        self.glosario = self._crear_glosario()
        self.ruta_datos = "datos_aprendizaje"
        self._crear_directorios()
    
    def _crear_directorios(self):
        """Crea los directorios necesarios para almacenar datos"""
        directorios = [
            self.ruta_datos,
            f"{self.ruta_datos}/usuarios",
            f"{self.ruta_datos}/progreso",
            f"{self.ruta_datos}/evaluaciones",
            f"{self.ruta_datos}/certificados"
        ]
        for dir in directorios:
            os.makedirs(dir, exist_ok=True)
    
    def _crear_glosario(self) -> Dict:
        """Crea un glosario de términos para principiantes"""
        return {
            "algoritmo": "Es como una receta de cocina: pasos ordenados para resolver un problema",
            "variable": "Es como una caja donde guardas información que puede cambiar",
            "función": "Es como una máquina: le das algo y te devuelve un resultado",
            "bucle": "Es repetir algo varias veces, como dar vueltas en círculo",
            "condición": "Es como un semáforo: si está verde haces algo, si está rojo haces otra cosa",
            "array": "Es como una fila de cajas numeradas donde guardas cosas",
            "debugging": "Es como ser detective: buscar y arreglar errores en tu código",
            "API": "Es como un mesero: pides algo y te trae lo que necesitas",
            "base de datos": "Es como un archivador gigante muy organizado",
            "framework": "Es como un kit de construcción con piezas pre-hechas"
        }
    
    def _crear_temario_completo(self) -> Dict:
        """Crea un temario súper completo desde cero hasta experto"""
        return {
            "nivel_0_absoluto_principiante": {
                "titulo": "🌱 EMPEZANDO DESDE CERO",
                "descripcion": "Para personas que nunca han tocado una computadora profesionalmente",
                "duracion_total": "2 semanas",
                "modulos": [
                    {
                        "id": "que_es_programar",
                        "titulo": "¿Qué es programar? Explicado como para un niño de 5 años",
                        "duracion": 45,
                        "contenido": {
                            "introduccion": """
                            Imagina que tienes un robot amigo. Este robot es muy obediente pero también
                            muy tonto - solo hace EXACTAMENTE lo que le dices. Si quieres que te haga
                            un sandwich, no puedes solo decirle 'hazme un sandwich'. Tienes que decirle:
                            1. Ve a la cocina
                            2. Abre el cajón del pan
                            3. Saca dos rebanadas
                            4. Abre la nevera... etc.
                            
                            ¡Eso es programar! Dar instrucciones súper específicas a una computadora.
                            """,
                            "conceptos_clave": [
                                "Las computadoras son tontas pero rápidas",
                                "Programar es dar instrucciones paso a paso",
                                "No hay magia, solo lógica"
                            ],
                            "ejemplos_cotidianos": [
                                "Receta de cocina = Programa",
                                "Instrucciones de IKEA = Algoritmo",
                                "GPS dando direcciones = Ejecución de código"
                            ],
                            "ejercicio_mental": "Escribe los pasos para lavarte los dientes",
                            "ejercicio_practico": "Juega a ser robot con un amigo dándole instrucciones"
                        }
                    },
                    {
                        "id": "computadora_amiga",
                        "titulo": "Tu computadora: de enemiga a mejor amiga",
                        "duracion": 60,
                        "contenido": {
                            "introduccion": """
                            La computadora no muerde, ¡lo prometo! Vamos a conocerla como si fuera
                            una nueva amiga. Aprenderás qué hace cada parte y por qué no debes
                            tenerle miedo.
                            """,
                            "partes_explicadas": {
                                "teclado": "Como un piano pero para escribir",
                                "mouse": "Tu mano virtual dentro de la pantalla",
                                "pantalla": "La ventana a mundos digitales",
                                "CPU": "El cerebro que piensa muy rápido",
                                "memoria": "Donde guarda lo que está pensando ahora",
                                "disco duro": "El baúl de los recuerdos permanentes"
                            },
                            "miedos_comunes": [
                                "No vas a romper nada haciendo clic",
                                "Los errores son normales y buenos para aprender",
                                "Ctrl+Z es tu mejor amigo (deshace cosas)"
                            ],
                            "ejercicios": [
                                "Abre y cierra 5 programas diferentes",
                                "Crea una carpeta con tu nombre",
                                "Escribe un documento y guárdalo"
                            ]
                        }
                    },
                    {
                        "id": "internet_basico",
                        "titulo": "Internet: El mundo en tu pantalla",
                        "duracion": 45,
                        "contenido": {
                            "introduccion": """
                            Internet es como una biblioteca gigante donde todos pueden poner y
                            leer libros. También es como una plaza donde puedes hablar con
                            personas de todo el mundo.
                            """,
                            "conceptos_simples": {
                                "navegador": "Tu vehículo para viajar por internet",
                                "URL": "La dirección de una casa en internet",
                                "buscador": "Tu guía turístico personal",
                                "email": "Tu buzón de correo digital"
                            },
                            "seguridad_basica": [
                                "No des información personal a extraños",
                                "Si algo parece demasiado bueno, probablemente es falso",
                                "Usa contraseñas como si fueran llaves de tu casa"
                            ],
                            "practica": [
                                "Busca '¿cómo hacer pizza casera?'",
                                "Envía un email a ti mismo",
                                "Marca 3 páginas web como favoritas"
                            ]
                        }
                    }
                ]
            },
            
            "nivel_1_principiante": {
                "titulo": "🌿 PRINCIPIANTE - Tus primeros pasos",
                "descripcion": "Ahora que conoces la computadora, vamos a empezar a programar",
                "duracion_total": "1 mes",
                "modulos": [
                    {
                        "id": "primer_programa",
                        "titulo": "Tu primer programa: ¡Hola Mundo!",
                        "duracion": 90,
                        "contenido": {
                            "introduccion": """
                            ¿Recuerdas el robot del que hablamos? Ahora le vamos a enseñar a
                            hablar. Empezaremos con algo simple: hacer que diga 'Hola Mundo'.
                            Es tradición que este sea el primer programa de todos.
                            """,
                            "paso_a_paso": [
                                "Abrimos un programa para escribir código (como Word pero para robots)",
                                "Escribimos: print('Hola Mundo')",
                                "Le damos al botón de 'play'",
                                "¡La computadora nos saluda!"
                            ],
                            "explicacion_detallada": {
                                "print": "Es como decirle a la computadora 'muestra esto en la pantalla'",
                                "comillas": "Todo lo que está entre comillas es texto literal",
                                "parentesis": "Es como un sobre donde metemos lo que queremos mostrar"
                            },
                            "variaciones": [
                                "print('Hola, me llamo [tu nombre]')",
                                "print('Tengo [tu edad] años')",
                                "print('Mi color favorito es el [color]')"
                            ],
                            "mini_proyecto": "Haz que la computadora se presente por ti con 5 frases"
                        }
                    },
                    {
                        "id": "variables_cajas_magicas",
                        "titulo": "Variables: Las cajas mágicas de la programación",
                        "duracion": 120,
                        "contenido": {
                            "introduccion": """
                            Imagina que tienes cajas mágicas donde puedes guardar cosas:
                            números, palabras, lo que sea. Y además, les puedes poner
                            etiquetas para acordarte qué hay dentro.
                            """,
                            "ejemplos_visuales": {
                                "nombre = 'Juan'": "Una caja llamada 'nombre' que contiene 'Juan'",
                                "edad = 25": "Una caja llamada 'edad' que contiene el número 25",
                                "tiene_mascota = True": "Una caja que dice si tienes mascota o no"
                            },
                            "tipos_de_cajas": {
                                "texto": "Para guardar palabras y frases (string)",
                                "numeros": "Para guardar números (int, float)",
                                "si_o_no": "Para guardar verdadero o falso (boolean)",
                                "listas": "Para guardar muchas cosas en orden (list)"
                            },
                            "analogias": [
                                "Variable de texto = Post-it con una nota",
                                "Variable numérica = Calculadora con un número en pantalla",
                                "Variable booleana = Interruptor de luz (prendido/apagado)"
                            ],
                            "ejercicios_progresivos": [
                                "Crea variables con tu información personal",
                                "Haz operaciones matemáticas con variables numéricas",
                                "Combina variables de texto para formar frases"
                            ]
                        }
                    },
                    {
                        "id": "decisiones_if",
                        "titulo": "Tomando decisiones: Si esto, entonces aquello",
                        "duracion": 150,
                        "contenido": {
                            "introduccion": """
                            En la vida real tomamos decisiones todo el tiempo:
                            SI llueve ENTONCES llevo paraguas.
                            SI tengo hambre ENTONCES como algo.
                            Las computadoras también pueden tomar decisiones así.
                            """,
                            "estructura_simple": """
                            if esta_lloviendo:
                                print('Lleva paraguas')
                            else:
                                print('Disfruta el sol')
                            """,
                            "ejemplos_cotidianos": [
                                "Cajero automático: SI tienes saldo ENTONCES puedes retirar dinero",
                                "Semáforo: SI está verde ENTONCES los autos pasan",
                                "Alarma: SI son las 7am ENTONCES suena"
                            ],
                            "comparaciones": {
                                "==": "¿Es igual a...?",
                                ">": "¿Es mayor que...?",
                                "<": "¿Es menor que...?",
                                "!=": "¿Es diferente de...?"
                            },
                            "proyecto_interactivo": """
                            Crear un programa que:
                            1. Pregunte tu edad
                            2. Si eres mayor de 18, diga 'Puedes votar'
                            3. Si no, diga cuántos años te faltan
                            """
                        }
                    }
                ]
            },
            
            "nivel_2_intermedio_bajo": {
                "titulo": "🌳 INTERMEDIO BÁSICO - Construyendo cimientos",
                "descripcion": "Ya sabes lo básico, ahora vamos a construir cosas más interesantes",
                "duracion_total": "2 meses",
                "modulos": [
                    {
                        "id": "bucles_repeticion",
                        "titulo": "Bucles: Hacer cosas muchas veces sin cansarte",
                        "duracion": 180,
                        "contenido": {
                            "introduccion": """
                            ¿Te imaginas escribir 'Hola' 1000 veces? ¡Qué aburrido!
                            Por suerte, podemos decirle a la computadora que lo haga
                            por nosotros. Eso son los bucles: repetir cosas.
                            """,
                            "tipos_de_bucles": {
                                "for": """
                                Como contar del 1 al 10:
                                for numero in range(1, 11):
                                    print(numero)
                                """,
                                "while": """
                                Como esperar hasta que algo pase:
                                while no_tengo_sueño:
                                    ver_otra_serie_en_netflix()
                                """
                            },
                            "analogias_reales": [
                                "Lavadora: Repite el ciclo de lavado varias veces",
                                "Playlist de música: Reproduce canciones una tras otra",
                                "Rutina de ejercicio: 3 series de 10 repeticiones"
                            ],
                            "proyectos": [
                                "Tabla de multiplicar automática",
                                "Contador regresivo para año nuevo",
                                "Dibujar patrones con asteriscos"
                            ]
                        }
                    }
                ]
            }
        }
    
    def explicar_concepto(self, concepto: str) -> str:
        """Explica cualquier concepto de forma simple"""
        if concepto.lower() in self.glosario:
            return self.glosario[concepto.lower()]
        else:
            return "Ese concepto aún no está en mi glosario, pero lo agregaré pronto!"
    
    def evaluar_comprension_interactiva(self, usuario_id: str, tema_id: str) -> int:
        """Evaluación más interactiva y amigable"""
        print("\n🎯 MOMENTO DE PRÁCTICA")
        print("No te preocupes, no es un examen. Solo quiero ver qué aprendiste.\n")
        
        puntuacion = 0
        
        # Pregunta 1: Explicar con tus palabras
        print("1️⃣ Explícame con TUS PROPIAS PALABRAS qué aprendiste hoy.")
        print("   (Como si se lo explicaras a tu abuela)")
        respuesta1 = input("\n   Tu explicación: ")
        
        if len(respuesta1) > 30:
            puntuacion += 30
            print("   ✨ ¡Excelente! Me encanta cómo lo explicaste.\n")
        else:
            puntuacion += 15
            print("   💡 Bien, pero podrías elaborar un poco más.\n")
        
        # Pregunta 2: Ejemplo práctico
        print("2️⃣ Dame un ejemplo de la VIDA REAL donde usarías esto.")
        respuesta2 = input("\n   Tu ejemplo: ")
        
        if "por ejemplo" in respuesta2.lower() or len(respuesta2) > 40:
            puntuacion += 35
            print("   🎉 ¡Genial ejemplo! Eso demuestra que lo entendiste.\n")
        else:
            puntuacion += 20
            print("   👍 Buen intento. Los ejemplos ayudan a fijar el conocimiento.\n")
        
        # Pregunta 3: Aplicación creativa
        print("3️⃣ Si fueras a enseñar esto a un niño de 10 años, ¿qué juego inventarías?")
        respuesta3 = input("\n   Tu idea: ")
        
        if len(respuesta3) > 20:
            puntuacion += 35
            print("   🌟 ¡Qué creativo! Enseñar es la mejor forma de aprender.\n")
        else:
            puntuacion += 20
            print("   💭 Interesante. La creatividad es clave en programación.\n")
        
        # Feedback motivacional
        print("\n" + "="*50)
        if puntuacion >= 90:
            print("🏆 ¡INCREÍBLE! Dominaste el tema completamente.")
            print("   Estás listo para el siguiente desafío.")
        elif puntuacion >= 70:
            print("🌟 ¡MUY BIEN! Entendiste los conceptos principales.")
            print("   Con un poco más de práctica serás experto.")
        elif puntuacion >= 50:
            print("👏 ¡BIEN HECHO! Vas por buen camino.")
            print("   Practica los ejercicios extra para reforzar.")
        else:
            print("🌱 ¡NO TE PREOCUPES! Todos aprendemos a nuestro ritmo.")
            print("   Volvamos a repasar juntos el tema.")
        
        return puntuacion
    
    def _guardar_usuario(self, usuario_id: str):
        """Guarda los datos del usuario en archivo"""
        try:
            archivo_usuario = f"{self.ruta_datos}/usuarios/{usuario_id}.json"
            with open(archivo_usuario, 'w', encoding='utf-8') as f:
                json.dump(self.usuarios[usuario_id], f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error al guardar usuario: {e}")
    
    def _cargar_usuario(self, usuario_id: str) -> bool:
        """Carga los datos del usuario desde archivo"""
        try:
            archivo_usuario = f"{self.ruta_datos}/usuarios/{usuario_id}.json"
            if os.path.exists(archivo_usuario):
                with open(archivo_usuario, 'r', encoding='utf-8') as f:
                    self.usuarios[usuario_id] = json.load(f)
                return True
            return False
        except Exception as e:
            print(f"❌ Error al cargar usuario: {e}")
            return False
    
    def registrar_usuario(self, nombre: str, email: str) -> str:
        """Registra un nuevo usuario con bienvenida especial"""
        usuario_id = f"user_{len(self.usuarios) + 1}"
        self.usuarios[usuario_id] = {
            "nombre": nombre,
            "email": email,
            "fecha_registro": datetime.now().isoformat(),
            "nivel_actual": "nivel_0_absoluto_principiante",
            "progreso": {},
            "evaluaciones_completadas": [],
            "puntuacion_total": 0,
            "logros": [],
            "retos_completados": [],
            "preferencias": {
                "modo_aprendizaje": "visual",
                "tiempo_diario": 30,
                "recordatorios": True
            }
        }
        
        self._guardar_usuario(usuario_id)
        
        # Bienvenida especial
        print(f"\n🎉 ¡BIENVENIDO/A {nombre.upper()}!")
        print("="*50)
        print("🌟 Has dado el primer paso en tu viaje para convertirte")
        print("   en un programador diferencial.")
        print("\n📚 En este sistema aprenderás:")
        print("   • Desde los conceptos más básicos")
        print("   • Con explicaciones súper claras") 
        print("   • A tu propio ritmo")
        print("   • Con proyectos divertidos")
        print("\n🎯 Tu ID único es: " + usuario_id)
        print("   (Guárdalo para volver a entrar)")
        
        time.sleep(2)
        
        return usuario_id
    
    def iniciar_sesion(self, usuario_id: str) -> bool:
        """Inicia sesión con un usuario existente"""
        if self._cargar_usuario(usuario_id):
            print(f"\n✅ ¡Bienvenido de vuelta, {self.usuarios[usuario_id]['nombre']}!")
            return True
        else:
            print("\n❌ Usuario no encontrado. Verifica tu ID.")
            return False
    
    def estudiar_tema(self, usuario_id: str, tema_id: str):
        """Estudiar un tema específico"""
        usuario = self.usuarios[usuario_id]
        
        # Buscar el tema en todos los niveles
        tema_encontrado = None
        for nivel in self.modulos.values():
            for modulo in nivel['modulos']:
                if modulo['id'] == tema_id:
                    tema_encontrado = modulo
                    break
            if tema_encontrado:
                break
        
        if not tema_encontrado:
            print("❌ Tema no encontrado.")
            return
        
        print("\n" + "="*60)
        print(f"📖 {tema_encontrado['titulo']}")
        print("="*60)
        print(f"⏱️ Duración estimada: {tema_encontrado['duracion']} minutos")
        
        # Mostrar contenido
        contenido = tema_encontrado['contenido']
        
        if 'introduccion' in contenido:
            print("\n🌟 INTRODUCCIÓN:")
            print(contenido['introduccion'])
        
        if 'conceptos_clave' in contenido:
            print("\n🔑 CONCEPTOS CLAVE:")
            for concepto in contenido['conceptos_clave']:
                print(f"   • {concepto}")
        
        if 'ejemplos_cotidianos' in contenido:
            print("\n🏠 EJEMPLOS DE LA VIDA REAL:")
            for ejemplo in contenido['ejemplos_cotidianos']:
                print(f"   • {ejemplo}")
        
        input("\n⏸️ Presiona Enter cuando termines de leer...")
        
        # Evaluación
        puntuacion = self.evaluar_comprension_interactiva(usuario_id, tema_id)
        
        # Actualizar progreso
        usuario['progreso'][tema_id] = {
            'fecha_completado': datetime.now().isoformat(),
            'puntuacion': puntuacion,
            'tiempo_estudio': tema_encontrado['duracion']
        }
        usuario['puntuacion_total'] += puntuacion
        
        self._guardar_usuario(usuario_id)
        
        print(f"\n✅ Tema completado! +{puntuacion} puntos")
    
    def recomendar_siguiente_paso(self, usuario_id: str) -> str:
        """Recomienda el siguiente paso en el aprendizaje"""
        usuario = self.usuarios[usuario_id]
        nivel_actual = usuario['nivel_actual']
        
        if nivel_actual in self.modulos:
            modulos_nivel = self.modulos[nivel_actual]['modulos']
            
            # Buscar el primer módulo no completado
            for modulo in modulos_nivel:
                if modulo['id'] not in usuario['progreso']:
                    return f"📖 {modulo['titulo']}"
            
            # Si completó todos los módulos del nivel, pasar al siguiente
            niveles = list(self.modulos.keys())
            idx_actual = niveles.index(nivel_actual)
            
            if idx_actual < len(niveles) - 1:
                siguiente_nivel = niveles[idx_actual + 1]
                usuario['nivel_actual'] = siguiente_nivel
                self._guardar_usuario(usuario_id)
                
                primer_modulo = self.modulos[siguiente_nivel]['modulos'][0]
                return f"🎉 ¡Nuevo nivel desbloqueado! 📖 {primer_modulo['titulo']}"
            else:
                return "🏆 ¡Has completado todo el programa! Eres un experto."
        
        return "📚 Comienza con los fundamentos básicos"
    
    def ver_progreso_detallado(self, usuario_id: str):
        """Muestra el progreso detallado del usuario"""
        usuario = self.usuarios[usuario_id]
        
        print("\n" + "="*60)
        print(f"📊 PROGRESO DETALLADO DE {usuario['nombre'].upper()}")
        print("="*60)
        
        print(f"\n👤 PERFIL:")
        print(f"   📧 Email: {usuario['email']}")
        print(f"   📅 Registrado: {usuario['fecha_registro'][:10]}")
        print(f"   🎯 Nivel actual: {usuario['nivel_actual'].replace('_', ' ').title()}")
        print(f"   ⭐ Puntos totales: {usuario['puntuacion_total']}")
        
        print(f"\n📚 TEMAS COMPLETADOS:")
        if usuario['progreso']:
            for tema_id, progreso in usuario['progreso'].items():
                fecha = progreso['fecha_completado'][:10]
                puntos = progreso['puntuacion']
                print(f"   ✅ {tema_id}: {puntos} puntos ({fecha})")
        else:
            print("   🌱 Aún no has completado ningún tema. ¡Empecemos!")
        
        # Mostrar siguiente paso
        siguiente = self.recomendar_siguiente_paso(usuario_id)
        print(f"\n🎯 SIGUIENTE PASO:")
        print(f"   {siguiente}")
    
    def mostrar_informacion_sistema(self):
        """Muestra información sobre el sistema"""
        print("\n" + "="*60)
        print("🤔 ¿QUÉ ES EL SISTEMA DE APRENDIZAJE PYTHONIA?")
        print("="*60)
        
        print("""
🎯 OBJETIVO:
   Convertirte en un programador diferencial desde CERO absoluto.
   
🌟 ¿QUÉ LO HACE ESPECIAL?
   • Explicaciones como para un niño de 5 años
   • Sin conocimientos previos necesarios
   • Proyectos divertidos y prácticos
   • Avance a tu propio ritmo
   • Sistema de logros y motivación
   
📚 NIVELES DE APRENDIZAJE:
   🌱 Nivel 0: Absoluto principiante (2 semanas)
   🌿 Nivel 1: Principiante (1 mes)
   🌳 Nivel 2: Intermedio básico (2 meses)
   🌲 Nivel 3: Intermedio (3 meses)
   🏔️ Nivel 4: Avanzado (4 meses)
   ⭐ Nivel 5: Experto (6 meses)
   
🎮 CARACTERÍSTICAS:
   • Evaluaciones interactivas (no exámenes aburridos)
   • Proyectos personalizados según tus intereses
   • Sistema de logros y recompensas
   • Comunidad virtual de aprendizaje
   • Asistente IA para resolver dudas
   • Retos diarios para practicar
   
💡 FILOSOFÍA:
   "Aprender programación debe ser divertido, no frustrante.
    Todos pueden ser programadores con la explicación correcta."
        """)
        
        input("\n⏸️ Presiona Enter para continuar...")
    
    def menu_principal_mejorado(self):
        """Menú principal mejorado con más opciones"""
        usuario_actual = None
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("\n" + "="*60)
            print("🚀 SISTEMA DE APRENDIZAJE ADAPTATIVO - PYTHONIA")
            print("="*60)
            
            if not usuario_actual:
                print("\n📚 Aprende programación desde CERO hasta EXPERTO")
                print("   Sin conocimientos previos necesarios")
                print("   Explicaciones claras como para un niño de 5 años")
                print("   Proyectos divertidos y prácticos")
                
                print("\n1. 🆕 Soy nuevo/a - Registrarme")
                print("2. 🔑 Ya tengo cuenta - Ingresar")
                print("3. 🤔 ¿Qué es esto? - Más información")
                print("0. 🚪 Salir")
                
                opcion = input("\n🎯 Tu elección: ")
                
                if opcion == "1":
                    print("\n📝 REGISTRO DE NUEVO USUARIO")
                    nombre = input("👤 Tu nombre: ").strip()
                    email = input("📧 Tu email: ").strip()
                    
                    if nombre and email:
                        usuario_actual = self.registrar_usuario(nombre, email)
                        input("\n⏸️ Presiona Enter para continuar...")
                    else:
                        print("❌ Por favor completa todos los campos.")
                        time.sleep(2)
                
                elif opcion == "2":
                    print("\n🔑 INICIAR SESIÓN")
                    usuario_id = input("🎯 Tu ID de usuario: ").strip()
                    
                    if self.iniciar_sesion(usuario_id):
                        usuario_actual = usuario_id
                        time.sleep(2)
                    else:
                        time.sleep(2)
                
                elif opcion == "3":
                    self.mostrar_informacion_sistema()
                
                elif opcion == "0":
                    print("\n👋 ¡Hasta luego! Sigue aprendiendo.")
                    break
                
                else:
                    print("❌ Opción no válida.")
                    time.sleep(1)
            
            else:
                usuario = self.usuarios[usuario_actual]
                print(f"\n👋 Hola {usuario['nombre']}!")
                print(f"   Nivel: {usuario['nivel_actual'].replace('_', ' ').title()}")
                print(f"   Puntos: {usuario['puntuacion_total']} ⭐")
                
                print("\n📚 APRENDIZAJE:")
                print("4. 🎯 Continuar donde lo dejé")
                print("5. 📖 Estudiar tema específico")
                print("6. 🗺️ Ver mi ruta completa")
                print("7. 📊 Mi progreso detallado")
                
                print("\n🎮 PRÁCTICA:")
                print("8. 💡 Reto diario")
                print("9. 🛠️ Proyecto personalizado")
                print("10. 🧪 Modo práctica libre")
                
                print("\n👥 COMUNIDAD:")
                print("11. 💬 Ver comunidad")
                print("12. 🤖 Preguntar al asistente")
                print("13. 🏆 Mis logros")
                
                print("\n⚙️ CONFIGURACIÓN:")
                print("14. 👤 Mi perfil")
                print("15. 🚪 Cerrar sesión")
                print("0. 🚪 Salir del programa")
                
                opcion = input("\n🎯 Tu elección: ")
                
                if opcion == "4":
                    siguiente = self.recomendar_siguiente_paso(usuario_actual)
                    if "completado todo" in siguiente:
                        print(siguiente)
                        input("\n⏸️ Presiona Enter para continuar...")
                    else:
                        # Extraer el ID del tema del siguiente paso
                        tema_id = self.obtener_siguiente_tema_id(usuario_actual)
                        if tema_id:
                            self.estudiar_tema(usuario_actual, tema_id)
                        else:
                            print("❌ No se pudo determinar el siguiente tema.")
                            time.sleep(2)
                
                elif opcion == "5":
                    self.mostrar_menu_temas(usuario_actual)
                
                elif opcion == "6":
                    self.mostrar_ruta_completa(usuario_actual)
                
                elif opcion == "7":
                    self.ver_progreso_detallado(usuario_actual)
                    input("\n⏸️ Presiona Enter para continuar...")
                
                elif opcion == "8":
                    reto = self.mini_retos_diarios()
                    self.ejecutar_reto_diario(usuario_actual, reto)
                
                elif opcion == "9":
                    proyecto = self.generar_proyecto_personalizado(usuario_actual, usuario['nivel_actual'])
                    self.ejecutar_proyecto_personalizado(usuario_actual, proyecto)
                
                elif opcion == "10":
                    self.modo_practica_libre(usuario_actual)
                
                elif opcion == "11":
                    self.comunidad_virtual(usuario_actual)
                    input("\n⏸️ Presiona Enter para continuar...")
                
                elif opcion == "12":
                    self.chat_con_asistente(usuario_actual)
                
                elif opcion == "13":
                    self.sistema_logros(usuario_actual)
                    input("\n⏸️ Presiona Enter para continuar...")
                
                elif opcion == "14":
                    self.gestionar_perfil(usuario_actual)
                
                elif opcion == "15":
                    print(f"\n👋 ¡Hasta luego, {usuario['nombre']}!")
                    usuario_actual = None
                    time.sleep(2)
                
                elif opcion == "0":
                    print(f"\n👋 ¡Hasta luego, {usuario['nombre']}! Sigue aprendiendo.")
                    break
                
                else:
                    print("❌ Opción no válida.")
                    time.sleep(1)
    
    def obtener_siguiente_tema_id(self, usuario_id: str) -> Optional[str]:
        """Obtiene el ID del siguiente tema a estudiar"""
        usuario = self.usuarios[usuario_id]
        nivel_actual = usuario['nivel_actual']
        
        if nivel_actual in self.modulos:
            modulos_nivel = self.modulos[nivel_actual]['modulos']
            
            # Buscar el primer módulo no completado
            for modulo in modulos_nivel:
                if modulo['id'] not in usuario['progreso']:
                    return modulo['id']
        
        return None
    
    def mostrar_menu_temas(self, usuario_id: str):
        """Muestra un menú para seleccionar temas específicos"""
        print("\n📚 SELECCIONAR TEMA ESPECÍFICO")
        print("="*50)
        
        todos_los_temas = []
        for nivel_id, nivel in self.modulos.items():
            for modulo in nivel['modulos']:
                todos_los_temas.append({
                    'id': modulo['id'],
                    'titulo': modulo['titulo'],
                    'nivel': nivel['titulo'],
                    'duracion': modulo['duracion']
                })
        
        for i, tema in enumerate(todos_los_temas, 1):
            completado = "✅" if tema['id'] in self.usuarios[usuario_id]['progreso'] else "🔲"
            print(f"{i:2d}. {completado} {tema['titulo']}")
            print(f"      📂 {tema['nivel']} | ⏱️ {tema['duracion']} min")
        
        try:
            seleccion = int(input(f"\n🎯 Selecciona un tema (1-{len(todos_los_temas)}): "))
            if 1 <= seleccion <= len(todos_los_temas):
                tema_seleccionado = todos_los_temas[seleccion - 1]
                self.estudiar_tema(usuario_id, tema_seleccionado['id'])
            else:
                print("❌ Selección no válida.")
                time.sleep(2)
        except ValueError:
            print("❌ Por favor ingresa un número válido.")
            time.sleep(2)
    
    def mostrar_ruta_completa(self, usuario_id: str):
        """Muestra la ruta completa de aprendizaje"""
        usuario = self.usuarios[usuario_id]
        
        print("\n🗺️ TU RUTA COMPLETA DE APRENDIZAJE")
        print("="*60)
        
        for nivel_id, nivel in self.modulos.items():
            # Estado del nivel
            modulos_nivel = nivel['modulos']
            completados = sum(1 for m in modulos_nivel if m['id'] in usuario['progreso'])
            total = len(modulos_nivel)
            
            if completados == total:
                estado_nivel = "✅ COMPLETADO"
            elif completados > 0:
                estado_nivel = f"🏃 EN PROGRESO ({completados}/{total})"
            else:
                estado_nivel = "🔒 PENDIENTE"
            
            print(f"\n{nivel['titulo']}")
            print(f"   {estado_nivel} | ⏱️ {nivel['duracion_total']}")
            print(f"   📝 {nivel['descripcion']}")
            
            # Mostrar módulos del nivel
            for modulo in modulos_nivel:
                icono = "✅" if modulo['id'] in usuario['progreso'] else "🔲"
                print(f"      {icono} {modulo['titulo']} ({modulo['duracion']} min)")
        
        input("\n⏸️ Presiona Enter para continuar...")
    
    def ejecutar_reto_diario(self, usuario_id: str, reto: Dict):
        """Ejecuta un reto diario"""
        print("\n🎯 RETO DIARIO")
        print("="*50)
        print(f"🏆 {reto['titulo']}")
        print(f"📝 {reto['descripcion']}")
        print(f"💡 Pista: {reto['pista']}")
        print(f"⭐ Puntos: {reto['puntos']}")
        print(f"🔥 Dificultad: {reto['dificultad']}")
        
        print("\n¿Estás listo para el reto?")
        respuesta = input("1. 💪 ¡Acepto el reto!  2. ⏰ Tal vez más tarde\n🎯 Tu elección: ")
        
        if respuesta == "1":
            print("\n🔥 ¡EXCELENTE! Tienes 15 minutos para completarlo.")
            print("Cuando termines, comparte tu solución:")
            
            solucion = input("\n📝 Tu código/solución:\n")
            
            if len(solucion) > 20:
                print(f"\n🎉 ¡Reto completado! +{reto['puntos']} puntos")
                self.usuarios[usuario_id]['puntuacion_total'] += reto['puntos']
                self.usuarios[usuario_id]['retos_completados'].append({
                    'reto': reto['titulo'],
                    'fecha': datetime.now().isoformat(),
                    'puntos': reto['puntos']
                })
                self._guardar_usuario(usuario_id)
            else:
                print("\n💭 Intenta dar más detalles en tu solución.")
        else:
            print("\n👍 ¡No problema! El reto estará aquí cuando estés listo.")
        
        input("\n⏸️ Presiona Enter para continuar...")
    
    def ejecutar_proyecto_personalizado(self, usuario_id: str, proyecto: Dict):
        """Ejecuta un proyecto personalizado"""
        print("\n🛠️ PROYECTO PERSONALIZADO")
        print("="*50)
        print(f"🎨 {proyecto['titulo']}")
        print(f"📝 {proyecto['descripcion']}")
        
        print("\n📋 PASOS DEL PROYECTO:")
        for i, paso in enumerate(proyecto['pasos'], 1):
            print(f"{i}. {paso}")
        
        print("\n¿Quieres empezar este proyecto?")
        respuesta = input("1. 🚀 ¡Empecemos!  2. 🔄 Otro proyecto  3. ⏰ Más tarde\n🎯 Tu elección: ")
        
        if respuesta == "1":
            print("\n🎯 ¡Perfecto! Vamos paso a paso:")
            
            for i, paso in enumerate(proyecto['pasos'], 1):
                print(f"\n📌 PASO {i}: {paso}")
                completado = input("¿Completaste este paso? (s/n): ").lower()
                
                if completado != 's':
                    print("💡 No te preocupes, toma tu tiempo. ¡Puedes volver cuando quieras!")
                    break
            else:
                print("\n🎉 ¡PROYECTO COMPLETADO! Eres increíble.")
                print("   +50 puntos por completar un proyecto personalizado!")
                self.usuarios[usuario_id]['puntuacion_total'] += 50
                self._guardar_usuario(usuario_id)
        
        elif respuesta == "2":
            nuevo_proyecto = self.generar_proyecto_personalizado(usuario_id, self.usuarios[usuario_id]['nivel_actual'])
            self.ejecutar_proyecto_personalizado(usuario_id, nuevo_proyecto)
        
        input("\n⏸️ Presiona Enter para continuar...")
    
    def modo_practica_libre(self, usuario_id: str):
        """Modo de práctica libre"""
        print("\n🧪 MODO PRÁCTICA LIBRE")
        print("="*50)
        print("🎮 Aquí puedes experimentar sin presión.")
        print("💡 Prueba código, haz preguntas, explora conceptos.")
        
        while True:
            print("\n¿Qué quieres hacer?")
            print("1. 💭 Explicar un concepto")
            print("2. 🔍 Buscar en el glosario")
            print("3. 📖 Repasar un tema")
            print("4. 🎲 Ejercicio aleatorio")
            print("5. 🚪 Volver al menú principal")
            
            opcion = input("\n🎯 Tu elección: ")
            
            if opcion == "1":
                concepto = input("\n🤔 ¿Qué concepto quieres que te explique? ")
                explicacion = self.explicar_concepto(concepto)
                print(f"\n💡 {explicacion}")
            
            elif opcion == "2":
                print("\n📚 GLOSARIO DISPONIBLE:")
                for termino, definicion in self.glosario.items():
                    print(f"   🔹 {termino}: {definicion}")
            
            elif opcion == "3":
                self.mostrar_menu_temas(usuario_id)
                break
            
            elif opcion == "4":
                ejercicios = [
                    "Crea una variable con tu edad y muéstrala en pantalla",
                    "Haz un programa que salude a 3 amigos diferentes",
                    "Crea una lista con tus 5 comidas favoritas",
                    "Programa que diga si un número es par o impar",
                    "Contador que cuente del 1 al 10"
                ]
                ejercicio = random.choice(ejercicios)
                print(f"\n🎲 EJERCICIO ALEATORIO:")
                print(f"   {ejercicio}")
                
                solucion = input("\n📝 Tu solución (o 'saltar'): ")
                if solucion.lower() != 'saltar':
                    print("👏 ¡Excelente práctica!")
            
            elif opcion == "5":
                break
            
            else:
                print("❌ Opción no válida.")
            
            input("\n⏸️ Presiona Enter para continuar...")
    
    def chat_con_asistente(self, usuario_id: str):
        """Chat con el asistente IA"""
        print("\n🤖 ASISTENTE PYTHONIA")
        print("="*50)
        print("💬 ¡Hola! Soy tu asistente virtual.")
        print("   Puedes preguntarme sobre programación, motivación, o lo que necesites.")
        print("   Escribe 'salir' para volver al menú principal.")
        
        while True:
            pregunta = input("\n💭 Tu pregunta: ").strip()
            
            if pregunta.lower() in ['salir', 'exit', 'quit']:
                print("👋 ¡Hasta luego! Siempre estaré aquí para ayudarte.")
                break
            
            if pregunta:
                respuesta = self.asistente_ia(pregunta)
                print(f"\n🤖 {respuesta}")
            else:
                print("🤔 No entendí tu pregunta. ¿Podrías ser más específico?")
    
    def gestionar_perfil(self, usuario_id: str):
        """Gestiona el perfil del usuario"""
        usuario = self.usuarios[usuario_id]
        
        while True:
            print("\n👤 GESTIÓN DE PERFIL")
            print("="*50)
            print(f"📝 Nombre: {usuario['nombre']}")
            print(f"📧 Email: {usuario['email']}")
            print(f"📅 Registro: {usuario['fecha_registro'][:10]}")
            print(f"🎯 Nivel: {usuario['nivel_actual'].replace('_', ' ').title()}")
            print(f"⭐ Puntos: {usuario['puntuacion_total']}")
            
            print("\n⚙️ PREFERENCIAS:")
            prefs = usuario['preferencias']
            print(f"🎨 Modo de aprendizaje: {prefs['modo_aprendizaje']}")
            print(f"⏰ Tiempo diario: {prefs['tiempo_diario']} minutos")
            print(f"🔔 Recordatorios: {'Sí' if prefs['recordatorios'] else 'No'}")
            
            print("\n¿Qué quieres cambiar?")
            print("1. 📝 Cambiar nombre")
            print("2. 📧 Cambiar email")
            print("3. 🎨 Modo de aprendizaje")
            print("4. ⏰ Tiempo de estudio diario")
            print("5. 🔔 Recordatorios")
            print("6. 📊 Ver estadísticas completas")
            print("7. 🚪 Volver al menú")
            
            opcion = input("\n🎯 Tu elección: ")
            
            if opcion == "1":
                nuevo_nombre = input("\n📝 Nuevo nombre: ").strip()
                if nuevo_nombre:
                    usuario['nombre'] = nuevo_nombre
                    print("✅ Nombre actualizado!")
            
            elif opcion == "2":
                nuevo_email = input("\n📧 Nuevo email: ").strip()
                if nuevo_email:
                    usuario['email'] = nuevo_email
                    print("✅ Email actualizado!")
            
            elif opcion == "3":
                print("\n🎨 Modos disponibles:")
                print("1. Visual (con emojis y colores)")
                print("2. Texto simple")
                print("3. Interactivo (muchas preguntas)")
                modo = input("🎯 Tu elección: ")
                modos = {"1": "visual", "2": "texto", "3": "interactivo"}
                if modo in modos:
                    usuario['preferencias']['modo_aprendizaje'] = modos[modo]
                    print("✅ Modo actualizado!")
            
            elif opcion == "4":
                try:
                    tiempo = int(input("\n⏰ Minutos por día (15-120): "))
                    if 15 <= tiempo <= 120:
                        usuario['preferencias']['tiempo_diario'] = tiempo
                        print("✅ Tiempo actualizado!")
                    else:
                        print("❌ Ingresa un tiempo entre 15 y 120 minutos.")
                except ValueError:
                    print("❌ Ingresa un número válido.")
            
            elif opcion == "5":
                recordar = input("\n🔔 ¿Quieres recordatorios? (s/n): ").lower()
                usuario['preferencias']['recordatorios'] = recordar == 's'
                print("✅ Preferencia actualizada!")
            
            elif opcion == "6":
                self.mostrar_estadisticas_completas(usuario_id)
            
            elif opcion == "7":
                break
            
            else:
                print("❌ Opción no válida.")
            
            if opcion in ["1", "2", "3", "4", "5"]:
                self._guardar_usuario(usuario_id)
                time.sleep(1)
    
    def mostrar_estadisticas_completas(self, usuario_id: str):
        """Muestra estadísticas completas del usuario"""
        usuario = self.usuarios[usuario_id]
        
        print("\n📊 ESTADÍSTICAS COMPLETAS")
        print("="*60)
        
        # Calcular estadísticas
        total_temas = len(usuario['progreso'])
        total_puntos = usuario['puntuacion_total']
        total_retos = len(usuario['retos_completados'])
        
        # Tiempo total estimado
        tiempo_total = sum(p.get('tiempo_estudio', 30) for p in usuario['progreso'].values())
        
        # Promedio de puntuación
        if total_temas > 0:
            promedio = sum(p.get('puntuacion', 0) for p in usuario['progreso'].values()) / total_temas
        else:
            promedio = 0
        
        print(f"📚 Temas completados: {total_temas}")
        print(f"⭐ Puntos totales: {total_puntos}")
        print(f"🎯 Retos completados: {total_retos}")
        print(f"⏱️ Tiempo total de estudio: {tiempo_total} minutos ({tiempo_total//60}h {tiempo_total%60}m)")
        print(f"📈 Promedio de puntuación: {promedio:.1f}/100")
        
        # Racha de estudio (simulada)
        racha_actual = random.randint(1, 15)
        racha_maxima = random.randint(racha_actual, 30)
        print(f"🔥 Racha actual: {racha_actual} días")
        print(f"🏆 Racha máxima: {racha_maxima} días")
        
        # Logros desbloqueados
        logros_totales = 7  # Número total de logros disponibles
        logros_usuario = len(usuario.get('logros', []))
        print(f"🏅 Logros: {logros_usuario}/{logros_totales}")
        
        # Nivel de maestría
        if total_puntos >= 1000:
            nivel_maestria = "🌟 Experto"
        elif total_puntos >= 500:
            nivel_maestria = "⭐ Avanzado"
        elif total_puntos >= 200:
            nivel_maestria = "🔥 Intermedio"
        elif total_puntos >= 50:
            nivel_maestria = "🌱 Principiante"
        else:
            nivel_maestria = "🐣 Novato"
        
        print(f"🎖️ Nivel de maestría: {nivel_maestria}")
        
        input("\n⏸️ Presiona Enter para continuar...")
    
    def generar_proyecto_personalizado(self, usuario_id: str, nivel: str) -> Dict:
        """Genera un proyecto personalizado según intereses del usuario"""
        
        print("\n🎨 PROYECTO PERSONALIZADO")
        print("Vamos a crear un proyecto especial para ti.\n")
        
        # Preguntar intereses
        print("¿Qué te gusta? (elige uno)")
        intereses = ["🎮 Videojuegos", "🎵 Música", "📚 Libros", "🍕 Comida", "⚽ Deportes"]
        for i, interes in enumerate(intereses, 1):
            print(f"{i}. {interes}")
        
        try:
            eleccion = input("\nTu elección (1-5): ")
        except:
            eleccion = "1"
        
        proyectos = {
            "1": {
                "titulo": "Tu Propio Juego de Aventuras",
                "descripcion": "Crea un juego donde el jugador toma decisiones",
                "pasos": [
                    "Diseña la historia con múltiples caminos",
                    "Crea el sistema de decisiones",
                    "Agrega un sistema de puntos",
                    "Incluye diferentes finales"
                ]
            },
            "2": {
                "titulo": "Playlist Manager Personal",
                "descripcion": "Organiza tu música como un DJ profesional",
                "pasos": [
                    "Crea listas de reproducción",
                    "Sistema de búsqueda por género",
                    "Reproduce canciones aleatoriamente",
                    "Guarda tus playlists favoritas"
                ]
            },
            "3": {
                "titulo": "Biblioteca Digital Personal",
                "descripcion": "Tu propio Goodreads casero",
                "pasos": [
                    "Registra libros leídos",
                    "Sistema de calificación",
                    "Notas sobre cada libro",
                    "Estadísticas de lectura"
                ]
            },
            "4": {
                "titulo": "Recetario Inteligente",
                "descripcion": "Tu chef personal digital",
                "pasos": [
                    "Guarda tus recetas favoritas",
                    "Busca por ingredientes",
                    "Calcula porciones automáticamente",
                    "Sugiere recetas según lo que tienes"
                ]
            },
            "5": {
                "titulo": "Estadísticas Deportivas Pro",
                "descripcion": "Analiza como un comentarista profesional",
                "pasos": [
                    "Registra resultados de partidos",
                    "Calcula estadísticas de jugadores",
                    "Predice resultados futuros",
                    "Crea gráficos de rendimiento"
                ]
            }
        }
        
        proyecto = proyectos.get(eleccion, proyectos["1"])
        return proyecto
    
    def sistema_logros(self, usuario_id: str) -> None:
        """Sistema de logros y recompensas para motivar"""
        usuario = self.usuarios[usuario_id]
        
        logros = {
            "primer_paso": {
                "nombre": "🐣 Primer Paso",
                "descripcion": "Completaste tu primer tema",
                "desbloqueado": len(usuario['progreso']) >= 1
            },
            "semana_constante": {
                "nombre": "🔥 En Racha",
                "descripcion": "Estudiaste 7 días seguidos",
                "desbloqueado": random.choice([True, False])  # Simulado
            },
            "nocturno": {
                "nombre": "🦉 Ave Nocturna",
                "descripcion": "Estudiaste después de las 10 PM",
                "desbloqueado": random.choice([True, False])  # Simulado
            },
            "perfeccionista": {
                "nombre": "💯 Perfeccionista",
                "descripcion": "100 puntos en una evaluación",
                "desbloqueado": any(p.get('puntuacion', 0) >= 100 for p in usuario['progreso'].values())
            },
            "explorador": {
                "nombre": "🗺️ Explorador",
                "descripcion": "Probaste todos los tipos de ejercicios",
                "desbloqueado": len(usuario['progreso']) >= 10
            },
            "mentor": {
                "nombre": "🎓 Mentor",
                "descripcion": "Ayudaste a otro estudiante",
                "desbloqueado": False
            },
            "innovador": {
                "nombre": "💡 Innovador",
                "descripcion": "Creaste tu propia solución única",
                "desbloqueado": usuario['puntuacion_total'] >= 500
            }
        }
        
        print("\n🏆 TUS LOGROS")
        print("="*50)
        
        desbloqueados = 0
        for logro in logros.values():
            if logro['desbloqueado']:
                print(f"✅ {logro['nombre']} - {logro['descripcion']}")
                desbloqueados += 1
            else:
                print(f"🔒 {logro['nombre']} - ???")
        
        print(f"\nLogros desbloqueados: {desbloqueados}/{len(logros)}")
        print(f"Nivel de Maestría: {'⭐' * (desbloqueados // 2)}")
    
    def comunidad_virtual(self, usuario_id: str) -> None:
        """Simula una comunidad de aprendizaje"""
        print("\n👥 COMUNIDAD PYTHONIA")
        print("="*50)
        
        mensajes_comunidad = [
            {
                "usuario": "Maria_Dev",
                "mensaje": "¡Acabo de completar mi primer bucle for! 🎉",
                "likes": 42
            },
            {
                "usuario": "CarlosCode",
                "mensaje": "Tip del día: print() es tu mejor amigo para debugging",
                "likes": 78
            },
            {
                "usuario": "Ana_Python",
                "mensaje": "¿Alguien más confundido con las listas al principio?",
                "likes": 23,
                "respuestas": [
                    "¡Yo también! Pero practicando se vuelve fácil",
                    "Piensa en ellas como cajones organizados"
                ]
            },
            {
                "usuario": "Luis_Learn",
                "mensaje": "Completé el proyecto de la calculadora 💪",
                "likes": 56
            }
        ]
        
        print("📢 Feed de la Comunidad:\n")
        for msg in mensajes_comunidad:
            print(f"👤 {msg['usuario']}")
            print(f"   {msg['mensaje']}")
            print(f"   ❤️ {msg['likes']} likes")
            if 'respuestas' in msg:
                for respuesta in msg['respuestas']:
                    print(f"   ↳ {respuesta}")
            print()
        
        accion = input("¿Quieres publicar algo? (s/n): ")
        if accion.lower() == 's':
            mensaje = input("Tu mensaje: ")
            print(f"\n✅ ¡Publicado! Tu mensaje ya está en la comunidad.")
            print("   ❤️ Maria_Dev le dio like a tu publicación")
    
    def asistente_ia(self, pregunta: str) -> str:
        """Asistente que responde preguntas comunes"""
        respuestas = {
            "error": """
            🤖 Los errores son tus amigos! Aquí van tips:
            1. Lee el mensaje completo del error
            2. Busca el número de línea mencionado
            3. Verifica ortografía y puntuación
            4. Googlea el error (todos lo hacemos)
            5. No te frustres, es parte del proceso
            """,
            "motivacion": """
            🌟 ¡Vas genial! Recuerda:
            - Todos empezamos desde cero
            - Cada error es una lección
            - La práctica hace al maestro
            - Tu ritmo es el correcto
            - ¡Ya has avanzado más de lo que crees!
            """,
            "tiempo": """
            ⏰ Sobre el tiempo de aprendizaje:
            - 30 min al día es mejor que 3 horas una vez
            - La consistencia gana a la intensidad
            - Descansa cuando lo necesites
            - Celebra pequeños logros
            - No hay prisa, disfruta el viaje
            """,
            "proyecto": """
            💡 Ideas para tu próximo proyecto:
            - Empieza simple y ve agregando features
            - Resuelve un problema personal
            - Copia algo que te guste y modifícalo
            - Pide feedback en la comunidad
            - No busques perfección, busca progreso
            """
        }
        
        # Buscar palabra clave en la pregunta
        pregunta_lower = pregunta.lower()
        for clave, respuesta in respuestas.items():
            if clave in pregunta_lower:
                return respuesta
        
        return """
        🤖 Hmm, no estoy seguro de entender tu pregunta.
        Intenta preguntar sobre:
        - Errores y debugging
        - Motivación para continuar
        - Tiempo de estudio
        - Ideas de proyectos
        """
    
    def mini_retos_diarios(self) -> Dict:
        """Genera mini retos diarios para práctica constante"""
        import random
        
        retos = [
            {
                "titulo": "🎯 Reto del Día: Hola Personalizado",
                "descripcion": "Haz que la computadora salude a 5 amigos diferentes",
                "pista": "Usa un bucle for y una lista de nombres",
                "dificultad": "Fácil",
                "puntos": 10
            },
            {
                "titulo": "🎲 Reto del Día: Dado Digital",
                "descripcion": "Crea un dado que tire números del 1 al 6",
                "pista": "Investiga sobre 'random.randint()'",
                "dificultad": "Fácil",
                "puntos": 15
            },
            {
                "titulo": "🔢 Reto del Día: Calculadora de Propinas",
                "descripcion": "Calcula automáticamente el 15% de propina",
                "pista": "Multiplica por 0.15",
                "dificultad": "Medio",
                "puntos": 20
            },
            {
                "titulo": "📝 Reto del Día: Lista de Tareas",
                "descripcion": "Crea una lista donde puedas agregar y quitar tareas",
                "pista": "Usa append() y remove()",
                "dificultad": "Medio",
                "puntos": 25
            },
            {
                "titulo": "🎮 Reto del Día: Piedra, Papel o Tijera",
                "descripcion": "Juega contra la computadora",
                "pista": "La computadora elige random, tú con input()",
                "dificultad": "Difícil",
                "puntos": 30
            }
        ]
        
        return random.choice(retos)
    
    def modo_historia(self, usuario_id: str, tema_id: str) -> None:
        """Presenta el contenido como una historia interactiva"""
        print("\n📖 MODO HISTORIA ACTIVADO")
        print("="*50)
        
        historias = {
            "variables_cajas_magicas": """
            🏰 LA LEYENDA DE LAS CAJAS MÁGICAS
            
            En el reino de Pythonia, existe una antigua magia llamada 'Variables'.
            
            Los magos de Pythonia descubrieron que podían crear cajas mágicas
            invisibles donde guardar cualquier cosa: números mágicos, palabras
            de poder, hasta decisiones importantes.
            
            Tu primera misión como aprendiz es crear tu propia caja mágica:
            
            >>> nombre_heroe = 'Sir Python'
            
            ¡Felicidades! Acabas de crear una caja llamada 'nombre_heroe' 
            y guardaste dentro el nombre 'Sir Python'.
            
            Ahora, cada vez que digas 'nombre_heroe', la magia te devolverá
            lo que guardaste dentro...
            
            [Presiona Enter para continuar tu aventura...]
            """,
            
            "bucles_repeticion": """
            ⚔️ LA BATALLA DE LOS MIL GUERREROS
            
            El malvado Wizard Bug ha invocado 1000 guerreros oscuros.
            ¿Deberás pelear con cada uno individualmente? ¡Por supuesto que no!
            
            Los antiguos magos crearon el hechizo 'For Loop':
            
            for guerrero in range(1000):
                lanzar_hechizo_luz()
            
            Con este poderoso conjuro, derrotas a todos los guerreros
            con un solo hechizo que se repite 1000 veces.
            
            ¡Pero cuidado! Si olvidas el límite, el hechizo podría
            repetirse para siempre (bucle infinito) y agotar tu magia...
            
            [Presiona Enter para aprender más hechizos...]
            """
        }
        
        if tema_id in historias:
            print(historias[tema_id])
            input()
        else:
            print("Esta historia aún está siendo escrita por los sabios...")
    
    def visualizador_progreso_visual(self, usuario_id: str) -> None:
        """Muestra el progreso de forma visual y motivadora"""
        usuario = self.usuarios[usuario_id]
        total_temas = sum(len(nivel['modulos']) for nivel in self.modulos.values())
        temas_completados = len(usuario['progreso'])
        porcentaje = (temas_completados / total_temas) * 100 if total_temas > 0 else 0
        
        print("\n🚀 TU VIAJE DE APRENDIZAJE")
        print("="*50)
        
        # Barra de progreso visual
        barra_length = 40
        completado = int((porcentaje / 100) * barra_length)
        barra = "█" * completado + "░" * (barra_length - completado)
        
        print(f"\nProgreso Total: [{barra}] {porcentaje:.1f}%")
        print(f"Temas Completados: {temas_completados}/{total_temas}")
        
        # Mapa del viaje
        print("\n🗺️ MAPA DE TU AVENTURA:")
        print("\n🏁 INICIO")
        
        niveles_nombres = {
            "nivel_0_absoluto_principiante": "🌱 Valle de los Principiantes",
            "nivel_1_principiante": "🌿 Bosque del Conocimiento",
            "nivel_2_intermedio_bajo": "🌳 Montañas de la Práctica",
            "nivel_3_intermedio": "🌲 Reino de las Aplicaciones",
            "nivel_4_avanzado": "🏔️ Cima de la Maestría",
            "nivel_5_experto": "⭐ Olimpo de los Expertos"
        }
        
        for nivel_id, nivel_nombre in niveles_nombres.items():
            if nivel_id in self.modulos:
                modulos_nivel = self.modulos[nivel_id]['modulos']
                completados_nivel = sum(1 for m in modulos_nivel if m['id'] in usuario['progreso'])
                total_nivel = len(modulos_nivel)
                
                if completados_nivel == total_nivel:
                    estado = "✅ COMPLETADO"
                elif completados_nivel > 0:
                    estado = f"🏃 EN PROGRESO ({completados_nivel}/{total_nivel})"
                else:
                    estado = "🔒 BLOQUEADO"
                
                print(f"├── {nivel_nombre}")
                print(f"│   {estado}")
        
        print("└── 🏆 FINAL: ¡Programador Diferencial!")
        
        # Siguiente objetivo
        print(f"\n🎯 PRÓXIMO OBJETIVO:")
        siguiente = self.recomendar_siguiente_paso(usuario_id)
        if isinstance(siguiente, str) and "completado" in siguiente:
            print("   ¡Has completado todo! Eres un maestro 🎓")
        else:
            print(f"   {siguiente}")
        
        # Estadísticas motivadoras
        print(f"\n📊 ESTADÍSTICAS ÉPICAS:")
        print(f"   ⚡ Puntos totales: {usuario['puntuacion_total']}")
        print(f"   🔥 Racha actual: {random.randint(1, 7)} días")
        print(f"   ⏱️ Tiempo total: {random.randint(10, 100)} horas")
        print(f"   🧠 Conceptos dominados: {len(usuario['progreso']) * 3}")
    
    def generar_certificado(self, usuario_id: str, nivel_completado: str) -> None:
        """Genera un certificado de completación"""
        usuario = self.usuarios[usuario_id]
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        
        certificado = f"""
        ╔══════════════════════════════════════════════════════════════╗
        ║                    🏆 CERTIFICADO DE LOGRO 🏆                ║
        ╠══════════════════════════════════════════════════════════════╣
        ║                                                              ║
        ║           Este certificado se otorga a:                      ║
        ║                                                              ║
        ║               {usuario['nombre'].upper():^30}               ║
        ║                                                              ║
        ║           Por completar exitosamente el:                     ║
        ║                                                              ║
        ║               {nivel_completado.replace('_', ' ').upper():^30}               ║
        ║                                                              ║
        ║           En el Sistema de Aprendizaje Pythonia              ║
        ║                                                              ║
        ║           Fecha: {fecha_actual:^30}                     ║
        ║           Puntos obtenidos: {usuario['puntuacion_total']:^19}          ║
        ║                                                              ║
        ║                    ⭐ PYTHONIA ACADEMY ⭐                    ║
        ╚══════════════════════════════════════════════════════════════╝
        """
        
        print(certificado)
        
        # Guardar certificado
        try:
            archivo_cert = f"{self.ruta_datos}/certificados/{usuario_id}_{nivel_completado}.txt"
            with open(archivo_cert, 'w', encoding='utf-8') as f:
                f.write(certificado)
            print(f"\n💾 Certificado guardado en: {archivo_cert}")
        except Exception as e:
            print(f"❌ Error al guardar certificado: {e}")
    
    def sistema_recompensas(self, usuario_id: str, puntos_ganados: int) -> None:
        """Sistema de recompensas por logros"""
        usuario = self.usuarios[usuario_id]
        
        recompensas = []
        
        # Recompensas por puntos totales
        puntos_totales = usuario['puntuacion_total']
        
        if puntos_totales >= 100 and puntos_totales - puntos_ganados < 100:
            recompensas.append("🎯 ¡Primera centena! Desbloqueaste el modo historia")
        
        if puntos_totales >= 500 and puntos_totales - puntos_ganados < 500:
            recompensas.append("🚀 ¡Quinientos puntos! Ahora puedes crear proyectos avanzados")
        
        if puntos_totales >= 1000 and puntos_totales - puntos_ganados < 1000:
            recompensas.append("👑 ¡Mil puntos! Eres oficialmente un MAESTRO de Pythonia")
        
        # Recompensas por temas completados
        temas_completados = len(usuario['progreso'])
        
        if temas_completados == 5:
            recompensas.append("📚 ¡Cinco temas dominados! Desbloqueaste el asistente avanzado")
        
        if temas_completados == 10:
            recompensas.append("🎓 ¡Diez temas! Ya puedes ser mentor de otros estudiantes")
        
        # Mostrar recompensas
        if recompensas:
            print("\n🎁 ¡NUEVAS RECOMPENSAS DESBLOQUEADAS!")
            print("="*50)
            for recompensa in recompensas:
                print(f"   {recompensa}")
            input("\n⏸️ Presiona Enter para continuar...")
    
    def exportar_progreso(self, usuario_id: str) -> None:
        """Exporta el progreso del usuario"""
        usuario = self.usuarios[usuario_id]
        fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        reporte = {
            "usuario": usuario['nombre'],
            "email": usuario['email'],
            "fecha_reporte": datetime.now().isoformat(),
            "estadisticas": {
                "temas_completados": len(usuario['progreso']),
                "puntos_totales": usuario['puntuacion_total'],
                "nivel_actual": usuario['nivel_actual'],
                "retos_completados": len(usuario['retos_completados'])
            },
            "progreso_detallado": usuario['progreso'],
            "logros": usuario.get('logros', []),
            "preferencias": usuario['preferencias']
        }
        
        try:
            archivo_reporte = f"{self.ruta_datos}/progreso/{usuario_id}_reporte_{fecha_actual}.json"
            with open(archivo_reporte, 'w', encoding='utf-8') as f:
                json.dump(reporte, f, indent=2, ensure_ascii=False)
            
            print(f"\n📊 Reporte de progreso exportado exitosamente!")
            print(f"📁 Ubicación: {archivo_reporte}")
            
        except Exception as e:
            print(f"❌ Error al exportar progreso: {e}")
    
    def importar_progreso(self, archivo_progreso: str) -> str:
        """Importa progreso desde un archivo"""
        try:
            with open(archivo_progreso, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            # Crear nuevo usuario con los datos importados
            usuario_id = f"imported_user_{len(self.usuarios) + 1}"
            self.usuarios[usuario_id] = {
                "nombre": datos.get('usuario', 'Usuario Importado'),
                "email": datos.get('email', 'email@ejemplo.com'),
                "fecha_registro": datetime.now().isoformat(),
                "nivel_actual": datos['estadisticas'].get('nivel_actual', 'nivel_0_absoluto_principiante'),
                "progreso": datos.get('progreso_detallado', {}),
                "evaluaciones_completadas": [],
                "puntuacion_total": datos['estadisticas'].get('puntos_totales', 0),
                "logros": datos.get('logros', []),
                "retos_completados": [],
                "preferencias": datos.get('preferencias', {
                    "modo_aprendizaje": "visual",
                    "tiempo_diario": 30,
                    "recordatorios": True
                })
            }
            
            self._guardar_usuario(usuario_id)
            
            print(f"\n✅ Progreso importado exitosamente!")
            print(f"🆔 Nuevo ID de usuario: {usuario_id}")
            
            return usuario_id
            
        except Exception as e:
            print(f"❌ Error al importar progreso: {e}")
            return None


# Función principal para ejecutar el sistema
def main():
    """Función principal para ejecutar el sistema"""
    print("🚀 Iniciando Sistema de Aprendizaje Pythonia...")
    time.sleep(1)
    
    sistema = SistemaAprendizajeCompleto()
    
    try:
        sistema.menu_principal_mejorado()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego! Gracias por usar Pythonia.")
        print("💡 Recuerda: la programación se aprende practicando.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        print("🔧 Por favor reporta este error al equipo de desarrollo.")


# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()