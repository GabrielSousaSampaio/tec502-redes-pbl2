<h1 align="center">
<br>Projeto: Transações Bancárias Distribuídas.
</h1>

<h4 align="center">
Projeto produzido a ser avaliado pela disciplina de M.I TEC 502 - Concorrência e Conectividade da Universidade Estadual de Feira de Santana. 
</h4>

 
<h2 align="center">
Implementação de um sistema distribuído e descentralizado para transações bancárias.
</h2>

<h1 id="sumario" align="center">Sumário</h1>
<ul>
  <li><a href="#introducao"> <b>Introdução</b></li>
	 <li><a href="#fundamentacao-teorica"> <b>Fundamentação Teórica</b> </a> </li>
<li><a href="#desenvolvimento"> <b>Desenvolvimento e Descrição em Alto Nível</b> </a> </li>
      <li><a href="#descricao-e-analise-dos-testes"> <b>Descrição e Análise dos Testes e Simulações, Resultados e Discussões</b> </a></li>
	      <li><a href="#conclusao"> <b>Conclusão</b> </a></li>
</ul>

<h1 id="introducao" align="center">Introdução</h1> 

 <p align="justify"> As transações bancárias são a espinha dorsal do sistema financeiro global, permitindo a transferência de valores entre contas e instituições financeiras de forma segura e eficiente. Com a crescente demanda por serviços financeiros rápidos e acessíveis, muitos bancos têm investido pesadamente em tecnologias avançadas para atender a essas expectativas. Essas tecnologias incluem inteligência artificial, machine learning, blockchain, APIs abertas, computação em nuvem e a utilização de sistemas distribuídos. 
  
No contexto das transações bancárias, garantir a integridade e a consistência dos dados é de suma importância. Para isso, as transações atômicas são fundamentais. Uma transação atômica é uma operação indivisível que deve ser completamente executada ou completamente revertida. Isso significa que, em uma transação bancária, todas as operações envolvidas, como a transferência de fundos de uma conta para outra, devem ser concluídas com sucesso ou não ser realizadas de forma alguma. Esse conceito é crucial para evitar discrepâncias e garantir que os saldos das contas permaneçam corretos mesmo em casos de falhas no sistema.

Além disso, como já havia sido citado anteriormente, uma das tecnologias que tem ganhado destaque para garantir a escalabilidade e a resiliência do sistema e das suas operações é o uso de sistemas distribuídos, onde múltiplos componentes de software ou hardware, localizados em diferentes máquinas, trabalham em conjunto para executar tarefas complexas. Em um ambiente distribuído, a responsabilidade é compartilhada entre vários nós da rede, o que aumenta a disponibilidade do serviço e reduz a dependência de um único ponto de falha.

Assim, o relatório abaixo descreve o processo de desenvolvimento de um sistema para gerenciamento de transações bancárias de maneira distribuída, abordando diversas funcionalidades essenciais, como criação de contas, login, visualização de informações de clientes e lógica de transações bancárias (depósito, retirada e transferência) de maneira atômica.</p>

<h1 id="fundamentacao-teorica" align="center">Fundamentação Teórica</h1>

<p align="justify">Durante a criação do projeto, foram empregados conceitos e recursos cruciais para assegurar seu desenvolvimento eficaz. Nesta seção, serão abordados tópicos essenciais que sustentam a construção do projeto, incluindo o conceito de Sistemas distribuídos, sistemas descentralizados e transações atômicas. Assim, a compreensão desses tópicos é fundamental para entender a execução e o funcionamento dos componentes do sistema de transações bancárias proposto.</p>

<h2>Sistemas Distribuídos</h2>

<p align="justify">Sistemas distribuídos são arquiteturas de software onde múltiplos componentes, localizados em diferentes máquinas de rede, trabalham em conjunto para alcançar um objetivo comum. Eles são projetados para fornecer serviços de forma transparente e coesa, distribuindo a carga de trabalho e os dados através de vários nós interconectados. 

Ademais, este tipo de sistema é amplamente utilizado para melhorar a escalabilidade, a resiliência e a disponibilidade dos serviços. As principais características dos sistemas distribuídos incluem transparência, escalabilidade, tolerância a falhas e consistência. Transparência significa que os usuários interagem com o sistema como se fosse um único ambiente unificado, sem consciência da distribuição dos componentes subjacentes. Escalabilidade refere-se à capacidade de dimensionar horizontalmente, adicionando mais nós à rede para aumentar a capacidade de processamento e armazenamento, essencial para lidar com grandes volumes de dados e alta demanda de usuários. 

A Tolerância a falhas nesses sistemas é aumentada pela distribuição dos componentes, permitindo que o sistema continue operando mesmo em caso de falhas em alguns dos nós, utilizando mecanismos de replicação de dados e redundância para assegurar a continuidade do serviço. A consistência e coordenação são desafios centrais em sistemas distribuídos, onde protocolos e algoritmos de sincronização são frequentemente empregados para garantir a integridade e a consistência dos dados.

Exemplos de sistemas distribuídos incluem sistemas de arquivos distribuídos como Google File System (GFS) e Hadoop Distributed File System (HDFS), bancos de dados distribuídos como Apache Cassandra e Amazon DynamoDB, e serviços de computação em nuvem oferecidos por AWS, Azure e Google Cloud. 

No entanto, existem desafios e considerações importantes, como latência e largura de banda, que podem impactar o desempenho, a segurança que exige o uso de criptografia, autenticação e controle de acesso robustos, e o gerenciamento de falhas, crucial para manter a operação contínua e a disponibilidade dos serviços. 

Em suma, os sistemas distribuídos são fundamentais para a construção de aplicações modernas que requerem alta escalabilidade, disponibilidade e resiliência, permitindo que serviços complexos sejam entregues de maneira eficiente e confiável, mesmo em face de falhas individuais e alta demanda.</p>

<h2>Sistemas descentralizados</h2>

<p align="justify">

Sistemas descentralizados são arquiteturas em que a tomada de decisão e o controle são distribuídos entre múltiplos nós ou entidades, sem depender de uma autoridade central. Essa abordagem contrasta com sistemas centralizados, onde um único ponto de controle regula todas as operações. 

A descentralização de um sistema visa aumentar a robustez, a transparência e a resistência à censura, além de reduzir a vulnerabilidade a falhas de um único ponto. Em um sistema descentralizado, cada nó opera de forma autônoma, mas de maneira coordenada com os demais, utilizando protocolos de consenso para assegurar que todas as partes concordem com o estado do sistema. 

Um exemplo clássico de sistemas descentralizados são as redes blockchain, como o Bitcoin e o Ethereum, onde as transações são verificadas e registradas por uma rede de nós, garantindo a integridade e a imutabilidade dos dados sem a necessidade de uma autoridade central. Outra aplicação de sistemas descentralizados é encontrada nas redes peer-to-peer (P2P), como BitTorrent, onde os recursos são compartilhados diretamente entre os usuários, eliminando a necessidade de servidores centrais.

Além disso, a descentralização oferece vários benefícios, incluindo a resistência a falhas, pois a ausência de um ponto único de falha significa que o sistema pode continuar operando mesmo que alguns nós falhem ou sejam comprometidos.Ela também promove a transparência, uma vez que todas as operações são registradas e podem ser auditadas por qualquer participante da rede. 

No entanto, sistemas descentralizados também enfrentam desafios significativos, como a necessidade de protocolos de consenso eficientes para evitar conflitos e garantir a consistência, a gestão de segurança em um ambiente aberto onde qualquer nó pode potencialmente participar, e a escalabilidade, uma vez que a coordenação entre muitos nós pode introduzir latência e complexidade. 

Em resumo, sistemas descentralizados representam uma evolução significativa nas arquiteturas de rede, promovendo um ambiente mais resiliente e transparente com aplicações que vão desde criptomoedas até redes de compartilhamento de arquivos, embora tragam consigo desafios que precisam ser cuidadosamente gerenciados para maximizar seu potencial.</p>


<h2>Transações Atômicas</h2>

<p align="justify">Transações atômicas são fundamentais em sistemas distribuídos para assegurar a integridade e a consistência dos dados durante operações críticas. O conceito central das transações atômicas é que todas as operações dentro de uma transação devem ser executadas como uma unidade indivisível. Isso significa que ou todas as operações são concluídas com sucesso, ou nenhuma delas é executada, revertendo quaisquer alterações realizadas até o ponto antes da transação começar.
Em ambientes distribuídos, onde várias partes independentes podem estar envolvidas em uma transação, garantir a atomicidade torna-se um desafio significativo. A coordenação entre diferentes nós é crucial para garantir que todos concordem com o resultado final da transação. Para assegurar essa coordenação são utilizados protocolos que garantam essa integridade. 
 
A importância das transações atômicas é evidente em cenários como sistemas financeiros, onde transferências de fundos entre bancos devem ser precisas e seguras. Se uma parte da transação falhar, garantir que todas as partes concordem em reverter quaisquer alterações é essencial para manter a integridade dos saldos e evitar discrepâncias nos registros financeiros.

Além dos sistemas financeiros tradicionais, tecnologias modernas como blockchains dependem fortemente de transações atômicas para garantir a execução correta e consistente de contratos inteligentes e outras operações descentralizadas. Em uma rede blockchain, onde a confiança é descentralizada e não há autoridade central, transações atômicas são essenciais para manter a imutabilidade e a integridade do ledger distribuído.

Portanto, entende-se que as transações atômicas são um pilar fundamental para a confiabilidade e a segurança de operações em sistemas distribuídos complexos. Elas proporcionam um mecanismo robusto para garantir que operações críticas sejam realizadas de forma confiável, mesmo em ambientes onde múltiplos componentes independentes podem estar envolvidos.</p>

<h2>Token Ring</h2>

<p align="justify">O Token Ring é uma tecnologia de rede de computadores que opera em um arranjo físico ou lógico de dispositivos conectados em forma de anel. Nesse tipo de rede, os dados são transmitidos em um único sentido ao redor do anel, de um dispositivo para o próximo, até que cheguem ao destino ou retornem ao emissor, dependendo do design específico da rede.
 
A característica distintiva do Token Ring é o uso de um "token" ou marcador, que circula continuamente pela rede. Apenas o dispositivo que possui o token tem permissão para transmitir dados. Isso garante que não ocorram colisões de dados, pois apenas um dispositivo pode transmitir de cada vez, mantendo a eficiência da rede.

Em termos de funcionamento, quando um dispositivo deseja transmitir dados, ele aguarda até que o token chegue até ele. Uma vez que o dispositivo possui o token, ele pode enviar seus dados para o próximo dispositivo na rede. Após a transmissão dos dados, o token é liberado e continua a circular pela rede, permitindo que outros dispositivos enviem dados quando for sua vez.
Dessa forma, o Token Ring oferece vantagens em termos de previsibilidade de desempenho, já que cada dispositivo tem um tempo predefinido para acessar o token e transmitir seus dados. Isso contrasta com as redes Ethernet, onde a competição por acesso ao meio de transmissão pode levar a colisões de dados e atrasos imprevistos.

Assim, o Token Ring, como protocolo de rede, pode ser vinculado aos sistemas distribuídos através de sua abordagem para controle de acesso ao meio. Em sistemas distribuídos, a coordenação eficiente e a prevenção de conflitos são essenciais para garantir a integridade das operações entre múltiplos nós. Assim como no Token Ring, onde apenas o dispositivo que possui o token pode transmitir dados, sistemas distribuídos utilizam mecanismos semelhantes de controle para evitar colisões de dados e garantir a consistência das transações.

Em um sistema distribuído, cada nó pode ser equiparado a um dispositivo no Token Ring, aguardando sua vez para acessar recursos compartilhados ou para realizar uma operação crítica. Protocolos de consenso em sistemas distribuídos, como o Two-Phase Commit (2PC) ou algoritmos baseados em blockchain, funcionam de maneira análoga ao token do Token Ring, garantindo que apenas um nó por vez possa realizar uma operação ou transação, mantendo assim a ordem e a consistência dos dados.
Embora o Token Ring seja mais diretamente aplicável a redes físicas, sua abordagem de controle de acesso ordenado e sequencial influencia a concepção de protocolos de coordenação em sistemas distribuídos. Esses sistemas dependem de uma comunicação precisa e de um gerenciamento eficiente de recursos para evitar conflitos e garantir a execução correta das operações, princípios que podem ser vistos refletidos em conceitos modernos de protocolos de consenso e governança distribuída.</p>

<h1 id="desenvolvimento" align="center">Desenvolvimento, metodologia, implementações e teses</h1>

<p align="justify">O projeto sobre transações bancárias distribuídas foi basicamente dividido em duas partes significativas: a criação das interfaces do banco e a criação dos servidores dos mesmos.</p>

<h2>INTERFACES</h2>

<p align="justify">A implementação inicial concentrou-se na criação de interfaces de usuário padronizadas para todas as operações bancárias, garantindo uma experiência consistente para o usuário final. Para atingir esse objetivo, utilizou-se templates HTML e estilização CSS com variáveis específicas para cada banco, permitindo personalização fácil das cores e logos. A arquitetura de template permite a reutilização do código, reduzindo a duplicação e facilitando a manutenção.
 
A interface de registro foi desenvolvida utilizando um formulário HTML que coleta informações do usuário, como nome, username, CPF/CNPJ, tipo de conta (física, jurídica ou conjunta) e senha. Este formulário envia uma requisição HTTP POST para o endpoint /register do servidor Flask. O servidor Flask do banco processa os dados recebidos, cria uma nova instância de cliente e a armazena o usuário em uma lista correspondente ao banco. A resposta do servidor, em formato JSON, indica o sucesso ou falha do registro, e a interface reage de acordo, exibindo mensagens apropriadas ao usuário.
 
A interface de “login” foi criada de maneira semelhante, com um formulário HTML que coleta o username e a senha do usuário. Este formulário envia uma requisição HTTP POST para o endpoint /login, onde o servidor Flask autentica o usuário verificando suas credenciais. Se a autenticação for bem-sucedida, o servidor responde com um JSON indicando sucesso, e o navegador do usuário é redirecionado para a página principal (/home). Caso contrário, uma mensagem de erro é exibida.

A página principal, ou “home”, exibe as informações do cliente logado, como tipo de conta, número da conta, nome, username, CPF/CNPJ e saldo. Estes dados são renderizados dinamicamente pelo servidor Flask utilizando o template HTML, que insere os valores apropriados nas variáveis Jinja. O servidor envia essas informações através de um endpoint protegido, geralmente /home, que requer que o usuário esteja autenticado (verificado por meio de sessões). A interface de home também inclui elementos para navegação, permitindo que o usuário acesse funções adicionais, como depósito, retirada e transferência.

Os endpoints utilizados para as operações bancárias são /deposit, /withdraw e /transfer, cada um recebendo requisições HTTP POST com os dados necessários em formato JSON. Para depósitos e retiradas, os dados incluem o número da conta e o valor da transação. Para transferências, os dados incluem os números das contas de origem e destino, além do valor a ser transferido. O servidor Flask processa essas requisições, atualiza os saldos das contas conforme necessário, e responde com um JSON indicando o sucesso ou falha da operação.</p>

<h2>SERVIDOR DOS BANCOS</h2>
<p align="justify">
O servidor dos bancos, representado pelo arquivo Bank, é a peça central que orquestra todas as operações e interações no sistema bancário. Este servidor foi implementado usando Flask, um framework de micro serviço em Python, que facilita a criação de aplicações web robustas e escaláveis.
 
Cada instância da classe Bank representa um banco individual, configurado com um nome único e seu próprio conjunto de clientes e contas. As principais variáveis dentro da classe Bank incluem self.name, que armazena o nome do banco, self.clients, que é uma lista de todas as contas associadas ao banco, e self.transactions_queue, que mantém as transações pendentes que serão processadas quando o banco adquirir o token.
 
O servidor define diversas rotas para interagir com a aplicação. Por exemplo, a rota /register é usada para registrar novas contas, recebendo dados do cliente via requisições HTTP POST em formato JSON. A função associada a esta rota valida os dados, cria uma nova instância da conta apropriada (como FisicPerson, JuridicPerson ou SharadAccount), e adiciona essa instância à lista de clientes do banco. Cada uma dessas classes citadas possuem atributos específicos e diferentes uma das outras, por isso sua criação foi necessária.
 
A rota /login autentica os usuários, verificando as credenciais fornecidas contra as armazenadas nas contas dos clientes. Se as credenciais forem válidas, uma sessão é iniciada, e o usuário é redirecionado para a página principal do banco.
A rota /home exibe as informações da conta do cliente autenticado. O servidor injeta os dados da conta na página HTML, personalizando a experiência do usuário com base no tipo de conta e outros atributos específicos.
 
Além das funções de registro e login, o servidor também define rotas para as operações bancárias, como depósito, retirada e transferência. Cada uma dessas operações é recebida via HTTP POST, validada, e adicionada à fila de transações do banco. A função handle_transaction, processa essas transações quando o banco possui o token.
 
A comunicação entre diferentes bancos na rede é facilitada por uma função que permite ao servidor do banco enviar e receber informações sobre clientes de outros bancos. Isso é crucial para operações como transferências interbancárias, onde os saldos de múltiplas contas em diferentes bancos precisam ser verificados e atualizados.
 
Em resumo, o servidor dos bancos, conforme implementado no arquivo Bank, é uma solução abrangente que gerencia todas as operações bancárias essenciais. Ele integra funcionalidades de registro, autenticação, transações financeiras e comunicação interbancária, proporcionando uma base sólida para um sistema bancário distribuído e eficiente.</p>

<h2>TOKEN RING E SISTEMAS DE TRANSAÇÕES</h2>

<p align="justify">
Para resolver questões de concorrência e garantir a integridade das transações, adotou-se uma abordagem de Token Ring. Cada banco mantém uma fila de transações que são processadas quando o banco possui o token, evitando conflitos e garantindo que todas as operações sejam executadas em uma ordem controlada. Esse modelo de controle distribuído é eficaz para ambientes sem um banco central de controle, permitindo que cada banco opere de maneira autônoma enquanto coopera com os outros na rede.
 
Nesse contexto, cada transação, seja depósito, retirada ou transferência, é representada por uma instância da classe Transaction. Esta classe encapsula detalhes como o tipo de transação, os bancos envolvidos e a quantia envolvida. Quando uma transação é iniciada pelo usuário através da interface, os dados da transação são enviados ao servidor do respectivo banco via requisições HTTP POST, e a transação é adicionada à fila do banco.

Cada banco na rede possui uma fila de transações pendentes que são processadas sequencialmente quando o banco possui o token. O token circula entre os bancos em um anel lógico, onde apenas o banco que detém o token pode processar sua fila de transações. Após processar todas as suas transações ou ao “expirar” o tempo de posse do token, o banco passa o token para o próximo banco na sequência.

Dessa forma, esse modelo também aborda questões de concorrência, uma vez que, cada banco só processa transações quando possui o token. Assim, evitam-se condições de corrida onde múltiplas transações possam tentar alterar o saldo de uma conta simultaneamente. A integridade das transações é mantida, garantindo que os saldos das contas sejam atualizados corretamente e que nenhuma transação seja perdida ou duplicada.

Logo, a implementação do Token Ring neste sistema bancário distribuído demonstra como técnicas de controle distribuído podem ser eficazes em garantir a integridade e a consistência das operações em ambientes sem um banco centralizado de controle. Essa abordagem permite que cada banco opere de forma autônoma enquanto ainda participa de um sistema cooperativo, proporcionando um modelo robusto e eficiente para gerenciar transações financeiras distribuídas.</p>

<h1 id="descricao-e-analise-dos-testes" align="center">Resultados e Discussões</h1>

O projeto, em seu estado final, exemplifica uma solução robusta e escalável para o gerenciamento de múltiplos bancos, integrando várias tecnologias e abordagens para garantir funcionalidade, segurança e eficiência. A utilização de Flask para o backend, templates HTML reutilizáveis para a interface, e um modelo distribuído de processamento de transações destacam-se como componentes chave desta solução, proporcionando uma base sólida para futuras expansões e melhorias. Ademais, destaca-se o uso do Token Ring, como uma solução simples e eficaz para o gerenciamento das transações bancárias, mantendo a integridade e proporcionando uma alternativa de escalabilidade futura no projeto.

Uma vez que o servidor do banco estiver funcionando, o uso da interface se dará através de uma interação simples e intuitiva por parte do usuário. Esse por sua vez, deve se redirecionar para a página de registro onde deverá criar uma conta de acordo com sua necessidade, podendo ser  então uma conta para pessoa física, pessoa jurídica ou uma conta conjunta. Após inserir os dados corretamente o usuário será levado até a tela de login onde poderá acessar sua conta. Uma vez logado, ele entrará na tela principal que conterá seus principais dados e funções como depositar, retirar e transferir. Essas interações serão feitas através de botões na interface.

Para garantir a funcionalidade e integridade do sistema foram produzidos os seguintes testes listados abaixo:

- Verificação da página de registro; 
- Verificação da página de login; 
- Verificação da função de depósito;
- Verificação da função de retirada; 
- Verificação da função de transferência com mais de um banco; 


Verificação da página de registro; 

Verificação da página de login; 

Verificação da função de depósito;

Verificação da função de retirada; 

Verificação da função de transferência com mais de um banco; 


<h1 id="conclusao" align="center">Conclusão</h1>

<p align="justify">
O desenvolvimento do projeto proposto demonstrou a importância e a complexidade dos sistemas distribuídos e do gerenciamento bancário ao integrar diversas funcionalidades e interfaces de usuário em uma aplicação web. A implementação de instâncias independentes para cada banco, rodando em diferentes portas ou máquinas, foi essencial para permitir a troca de informações em tempo real e garantir a escalabilidade do sistema, utilizando a infraestrutura de rede, bem como a manipulação de APIs REST para comunicação entre diferentes instâncias do Flask.
 
Ademais, a criação de interfaces padronizadas para múltiplos bancos, destacou a relevância de uma interface intuitiva para interação com os usuários. Além disso, os desafios enfrentados durante o desenvolvimento do projeto, como a escolha de métodos de transferência de fundos entre diferentes bancos e a garantia de integridade das transações, foram superados por meio da adoção de práticas de design cuidadosas e da utilização de tecnologias, tais como o Token Ring.

A lógica de transações, que inclui depósitos, retiradas e transferências interbancárias, foi implementada para garantir a segurança e a consistência dos saldos dos clientes. O uso de uma fila de transações e um modelo de Token Ring para controle de concorrência permitiu que cada banco processasse suas transações de maneira ordenada e sem conflitos, garantindo a integridade das operações.

Dessa forma, o projeto exemplifica uma solução robusta e escalável para o gerenciamento de múltiplos bancos, integrando várias tecnologias e abordagens para garantir funcionalidade, segurança e eficiência. A experiência adquirida ao longo do desenvolvimento oferece uma base sólida para futuras implementações e inovações no campo dos sistemas distribuídos e descentralizados.</p>

